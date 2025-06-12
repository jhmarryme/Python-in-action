from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# @title 定义天气智能体
# 使用前面定义的模型常量之一
AGENT_MODEL = 'openai/qwen2.5-72b-instruct'


# @title 定义 get_weather 工具
def get_weather(city: str) -> dict:
    """获取指定城市的当前天气报告。

    Args:
        city (str): 城市名称（例如，"New York"、"London"、"Tokyo"）。

    Returns:
        dict: 包含天气信息的字典。
              包含一个 'status' 键（'success' 或 'error'）。
              如果是 'success'，包含 'report' 键与天气详情。
              如果是 'error'，包含 'error_message' 键。
    """
    # 最佳实践：记录工具执行以便于调试
    print(f"--- Tool: get_weather called for city: {city} ---")
    city_normalized = city.lower().replace(" ", "")  # 基本输入标准化

    # 为简单起见的模拟天气数据
    mock_weather_db = {
        "newyork": {"status": "success", "report": "纽约的天气是晴朗的，温度为 25°C。"},
        "london": {"status": "success", "report": "伦敦多云，温度为 15°C。"},
        "tokyo": {"status": "success", "report": "东京有小雨，温度为 18°C。"},
    }

    # 最佳实践：在工具内优雅地处理潜在错误
    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    else:
        return {"status": "error", "error_message": f"抱歉，我没有 '{city}' 的天气信息。"}


# 工具使用示例（可选自测）
# print(get_weather("New York"))
# print(get_weather("Paris"))

# @title 定义天气智能体
root_agent = Agent(
    name="weather_agent_v1",
    model=LiteLlm(model=AGENT_MODEL),  # 指定底层 LLM
    description="为特定城市提供天气信息。",  # 对于稍后的任务分配至关重要
    instruction="你是一个有用的天气助手。你的主要目标是提供当前天气报告。"
                "当用户询问特定城市的天气时，"
                "你必须使用 'get_weather' 工具查找信息。"
                "分析工具的响应：如果状态为 'error'，礼貌地告知用户错误信息。"
                "如果状态为 'success'，向用户清晰简洁地呈现天气 'report'。"
                "仅在提到城市进行天气请求时使用该工具。",
    tools=[get_weather],  # 使该工具可用于此智能体
)
# Sample queries to test the agent:

# # Agent will give weather information for the specified cities.
# # What's the weather in Tokyo?
# # What is the weather like in London?
# # Tell me the weather in New York?

# # Agent will not have information for the specified city.
# # How about Paris?
