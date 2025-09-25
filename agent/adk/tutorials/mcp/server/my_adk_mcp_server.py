import asyncio
import json

import mcp.server.stdio
from dotenv import load_dotenv
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.load_web_page import load_web_page
from google.adk.tools.mcp_tool.conversion_utils import adk_to_mcp_tool_type
from mcp import types as mcp_types
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions

load_dotenv()

print("正在初始化 ADK load_web_page 工具...")
adk_tool_to_expose = FunctionTool(load_web_page)
print(f"ADK 工具 '{adk_tool_to_expose.name}' 已初始化并准备通过 MCP 暴露。")

print("正在创建 MCP 服务器实例...")
app = Server("adk-tool-exposing-mcp-server")


@app.list_tools()
async def list_mcp_tools() -> list[mcp_types.Tool]:
    """MCP handler to list tools this server exposes."""
    print("MCP 服务器：收到 list_tools 请求。")
    mcp_tool_schema = adk_to_mcp_tool_type(adk_tool_to_expose)
    print(f"MCP 服务器：广告工具：{mcp_tool_schema.name}")
    return [mcp_tool_schema]


# 实现 MCP 服务器的 handler 以执行工具调用
@app.call_tool()
async def call_mcp_tool(
        name: str, arguments: dict
) -> list[mcp_types.Any]:  # MCP 使用 mcp_types.Content
    """MCP handler to execute a tool call requested by an MCP client."""
    print(f"MCP 服务器：收到对 '{name}' 的 call_tool 请求，参数：{arguments}")

    if name == adk_tool_to_expose.name:
        try:
            adk_tool_response = await adk_tool_to_expose.run_async(
                args=arguments,
                tool_context=None,
            )
            print(f"MCP 服务器：ADK 工具 '{name}' 已执行。响应：{adk_tool_response}")

            response_text = json.dumps(adk_tool_response, indent=2)
            return [mcp_types.TextContent(type="text", text=response_text)]

        except Exception as e:
            print(f"MCP 服务器：执行 ADK 工具 '{name}' 时出错：{e}")
            error_text = json.dumps({"error": f"执行工具 '{name}' 失败：{str(e)}"})
            return [mcp_types.TextContent(type="text", text=error_text)]
    else:
        print(f"MCP 服务器：工具 '{name}' 未在此服务器中找到/暴露。")
        error_text = json.dumps({"error": f"工具 '{name}' 未在此服务器中实现。"})
        return [mcp_types.TextContent(type="text", text=error_text)]


async def run_mcp_stdio_server():
    """以标准输入/输出监听连接，运行 MCP 服务器。"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        print("MCP Stdio 服务器：开始与客户端握手...")
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=app.name,
                server_version="0.1.0",
                capabilities=app.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
        print("MCP Stdio 服务器：运行循环完成或客户端断开连接。")


if __name__ == "__main__":
    print("正在启动 MCP 服务器以通过 stdio 暴露 ADK 工具...")
    try:
        asyncio.run(run_mcp_stdio_server())
    except KeyboardInterrupt:
        print("\nMCP 服务器（stdio）被用户停止。")
    except Exception as e:
        print(f"MCP 服务器（stdio）遇到错误：{e}")
    finally:
        print("MCP 服务器（stdio）进程退出。")
