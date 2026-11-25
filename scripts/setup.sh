#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
chmod +x "$REPO_ROOT/scripts/post-commit.py"
ln -sf "../../scripts/post-commit.py" "$REPO_ROOT/.git/hooks/post-commit"
echo "Done! Git post-commit hook linked to scripts/post-commit.py"
