import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如果您没有配置环境变量，请在此处替换您的API-KEY
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务base_url
)

# 初始化messages列表
completion = client.chat.completions.create(
    model="qwen-long",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "system", "content": f"fileid://file-fe-c5a86afa89af4285bbf2315d"},  # 关联已上传文件
        {"role": "user", "content": "广东的住宿费标准是多少？"}
    ],
    stream=True,
    stream_options={"include_usage": True}
)

# 解析流式输出并计算Token消耗
full_content = ""
usage = None
for chunk in completion:
    if chunk.choices and chunk.choices[0].delta.content:
        full_content += chunk.choices[0].delta.content
    if chunk.usage:
        usage = chunk.usage

print("查询结果：", full_content)
print("Token消耗：")
print(f"输入Token（Prompt Tokens）: {usage.prompt_tokens}")
print(f"输出Token（Completion Tokens）: {usage.completion_tokens}")
print(f"总Token（Total Tokens）: {usage.total_tokens}")