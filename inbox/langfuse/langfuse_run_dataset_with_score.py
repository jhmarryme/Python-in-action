import asyncio
import os
from datetime import datetime
from typing import Literal

import aiohttp
import jieba
from langfuse import Langfuse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-78a056fb-a591-45fd-90af-f968267ae458"
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-61e7bff0-ea0f-4992-8c28-2b7a43cc41eb"
os.environ["LANGFUSE_HOST"] = "http://localhost:3010"


def calculate_similarity(text1, text2):
    # 分词
    texts = [" ".join(jieba.lcut(text1)), " ".join(jieba.lcut(text2))]

    # 使用TF-IDF向量化
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    # 计算余弦相似度
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosine_sim[0][0]


# 调用 dify 接口发送消息，获取 dify 响应
async def send_chat_message(
        query: str,
        inputs=None,
        url: str = os.getenv("DIFY_API_BASE", "http://127.0.0.1:5001/v1"),
        api_key: str = os.getenv("DIFY_API_KEY", "app-jQ5iPIuKT0s2bTDR64x2s2Ly"),
        response_mode: Literal["streaming", "blocking"] = "blocking",
        user: str = "auto_test",
        file_array=None,
):
    if file_array is None:
        file_array = []
    if inputs is None:
        inputs = {}
    chat_url = f"{url}/chat-messages"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "inputs": inputs,
        "query": query,
        "response_mode": response_mode,
        "conversation_id": "",
        "user": user,
        "files": file_array,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(chat_url, headers=headers, json=payload) as response:
            ret = await response.json()
            status = ret.get("status")
            message = ret.get("message")
            if status and message:
                raise ValueError(f"{status}: {message}")
            return ret


async def run_dataset_items(dataset, langfuse):
    run_name = 'test-{0}'.format(datetime.now().strftime("%Y%m%d-%H%M%S"))
    for item in dataset.items:
        response = await send_chat_message(item.input)
        # 将 dify 返回的 message_id 与 langfuse 中的 trace id 进行关联
        item.link(
            trace_or_observation=None,
            run_name=run_name,
            trace_id=response["message_id"],
            observation_id=None,
        )
        langfuse.score(
            trace_id=response["message_id"],
            name='cosine_sim',
            value=calculate_similarity(response['answer'], item.expected_output['answer']),
            comment='计算问题[' + item.input['text'] + ']的余弦相似度结果'
        )


if __name__ == '__main__':
    langfuse = Langfuse()
    dataset = langfuse.get_dataset("dify_dataset_1")
    asyncio.run(run_dataset_items(dataset, langfuse))
