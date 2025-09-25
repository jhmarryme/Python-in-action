import os

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp import StdioServerParameters

AGENT_MODEL = 'openai/qwen2.5-72b-instruct'
TARGET_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/home/jhmarryme/Downloads")

root_agent = LlmAgent(
    model=LiteLlm(model=AGENT_MODEL),
    name='filesystem_assistant_agent',
    instruction='帮助用户管理他们的文件。你可以列出文件、读取文件等。',
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='npx',
                    args=[
                        "-y",
                        "@modelcontextprotocol/server-filesystem",
                        os.path.abspath(TARGET_FOLDER_PATH),
                    ],
                ),
            ),
        )
    ],
)
