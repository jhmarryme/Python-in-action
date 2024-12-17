import os

from dotenv import load_dotenv
from mem0 import MemoryClient

load_dotenv()
m = MemoryClient(api_key=os.getenv("MEM0_API_KEY"))

# 从任何非结构化文本中存储记忆
result = m.add("我正在学习python,请推荐一些学习课程", user_id="wjh", metadata={"category": "study"})
print(result)
# 创建的记忆：正在学习Python
result = m.add("我喜欢玩switch双人游戏", user_id="wjh", metadata={"category": "hobbies"})
print(result)
# 创建的记忆：喜欢玩Switch双人游戏

# 搜索记忆
related_memories = m.search(query="wjh 最近在干嘛?", user_id="wjh")
print(related_memories)
related_memories = m.search(query="wjh 喜欢玩啥?", user_id="wjh")
print(related_memories)

# 获取记忆历史
all_memories = m.get_all(user_id="wjh")
print(all_memories)
