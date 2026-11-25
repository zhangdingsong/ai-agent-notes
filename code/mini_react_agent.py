"""30 行核心代码看清 ReAct Agent 的真实运转（零第三方依赖版）"""
import json, os, urllib.request

# 1. 本地真正的“手脚”函数 + 工具映射表
def get_weather(city: str) -> str:
    return {"杭州": "14°C，晴", "北京": "8°C，多云"}.get(city, "22°C，阴")

def calc(expr: str) -> str:
    return str(eval(expr, {"__builtins__": {}}))  # 仅作算术演示

TOOL_MAP = {"get_weather": get_weather, "calc": calc}

# 2. 给大模型看的“工具菜单”（JSON Schema）
TOOLS = [
    {"type": "function", "function": {"name": "get_weather", "description": "查城市实时天气",
     "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}},
    {"type": "function", "function": {"name": "calc", "description": "计算四则算术表达式",
     "parameters": {"type": "object", "properties": {"expr": {"type": "string"}}, "required": ["expr"]}}},
]

def call_llm(messages: list) -> dict:
    """有 API Key 时走真实大模型；未配置时走本地仿真（返回 100% 同款真实报文结构）"""
    api_key = os.getenv("LLM_API_KEY")
    if api_key:
        url = os.getenv("LLM_BASE_URL", "https://api.deepseek.com/chat/completions")
        model = os.getenv("LLM_MODEL", "deepseek-chat")
        body = json.dumps({"model": model, "messages": messages, "tools": TOOLS}).encode()
        req = urllib.request.Request(url, data=body, headers={
            "Authorization": f"Bearer {api_key}", "Content-Type": "application/json"
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())["choices"][0]["message"]

    # --- 本地仿真模式：原汁原味复现大模型 3 轮返回报文 ---
    n = len(messages)
    if n == 1:
        return {"role": "assistant", "content": None, "tool_calls": [
            {"id": "call_9x8a", "type": "function", "function": {"name": "get_weather", "arguments": '{"city": "杭州"}'}}]}
    if n == 3:
        return {"role": "assistant", "content": None, "tool_calls": [
            {"id": "call_2b7f", "type": "function", "function": {"name": "calc", "arguments": '{"expr": "20 - 14"}'}}]}
    return {"role": "assistant", "content": "杭州今天 14°C（晴），低于 20°C，距离 20°C 还差 6 度。"}

# 3. 核心 ReAct Loop（对应 01 笔记里的 while 循环 + max_steps 保险丝）
def run_agent(user_prompt: str, max_steps: int = 5):
    messages = [{"role": "user", "content": user_prompt}]
    for step in range(1, max_steps + 1):
        print(f"\n========== 第 {step} 轮思考 (当前黑板共 {len(messages)} 条消息) ==========")
        reply = call_llm(messages)
        messages.append(reply)  # 把模型的回复（哪怕是点单条）原样贴上黑板

        if not reply.get("tool_calls"):  # 没点单 = 大功告成！
            print(f"✅ [Final Answer]: {reply['content']}")
            return messages

        for tc in reply["tool_calls"]:   # 逐张处理模型开出的点单条
            fn_name = tc["function"]["name"]
            fn_args = json.loads(tc["function"]["arguments"])
            print(f"🛠️  [Action] 模型点单: {fn_name}({fn_args}) | 取餐号: {tc['id']}")
            obs = TOOL_MAP[fn_name](**fn_args)
            print(f"👀 [Observation] 本地执行结果: {obs}")
            messages.append({"role": "tool", "tool_call_id": tc["id"], "content": obs})

if __name__ == "__main__":
    final_board = run_agent("杭州今天几度？如果低于 20 度帮我算算差几度到 20 度。")
    print("\n📜 最终完整 messages[] 黑板 JSON：")
    print(json.dumps(final_board, ensure_ascii=False, indent=2))
