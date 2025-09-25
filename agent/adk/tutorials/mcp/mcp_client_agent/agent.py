from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp import StdioServerParameters

PATH_TO_YOUR_MCP_SERVER_SCRIPT = "/home/jhmarryme/develop/code/Python-in-action/agent/adk/tutorials/mcp/server/my_adk_mcp_server.py"

AGENT_MODEL = 'openai/qwen2.5-72b-instruct'
root_agent = LlmAgent(
    model=LiteLlm(model=AGENT_MODEL),
    name='web_reader_mcp_client_agent',
    instruction="使用 'load_web_page' 工具从用户提供的 URL 获取内容。",
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='/home/jhmarryme/develop/code/Python-in-action/agent/adk/.venv/bin/python',
                    args=[PATH_TO_YOUR_MCP_SERVER_SCRIPT],
                )
            )
            # tool_filter=['load_web_page'] # 可选：仅加载特定工具
        )
    ],
)
