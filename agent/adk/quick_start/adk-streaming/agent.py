from google.adk.agents import Agent
from google.adk.tools import google_search  # 导入工具

root_agent = Agent(
   # 智能体的唯一名称
   name="basic_search_agent",
   # 智能体将使用的大型语言模型 (LLM)
   model="gemini-2.0-flash-exp",
   # model="gemini-2.0-flash-live-001",  # 2025 年 2 月起的新流式模型版本
   # 智能体目的的简短描述
   description="使用 Google 搜索回答问题的智能体。",
   # 设置智能体行为的指令
   instruction="你是一位专业研究人员。你总是坚持事实。",
   # 添加 google_search 工具，使用 Google 搜索进行接地
   tools=[google_search]
)