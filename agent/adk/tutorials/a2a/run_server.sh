#!/usr/bin/env bash
set -euo pipefail

# 在项目根（包含 tutorials/）运行：
# bash tutorials/a2a/exposing/run_server.sh
cd ../../

# 访问 http://localhost:8001/.well-known/agent-card.json
exec .venv/bin/uvicorn tutorials.a2a.exposing.roll_agent.agent:a2a_app --host localhost --port 8001
# 访问 http://localhost:8002/a2a/api_server_agent/.well-known/agent-card.json
exec .venv/bin/adk api_server --a2a --port 8002 tutorials/a2a/exposing --log_level debug