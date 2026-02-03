import csv
import uuid
import requests
import time
import json
import re

API_URL = "http://localhost:8080/api/chat/chat-message"  # 修改为你的后端实际地址
BEARER_TOKEN = ""  # 在这里填写你的token，如有

# 读取CSV，按group分组
def read_questions(filename):
    groups = {}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            group = row['group']
            if group not in groups:
                groups[group] = []
            groups[group].append({'question': row['question'], 'answer': row['answer']})
    return groups

def decode_obj(obj):
    if isinstance(obj, dict):
        return {k: decode_obj(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [decode_obj(i) for i in obj]
    elif isinstance(obj, str):
        try:
            return obj.encode('latin1').decode('utf-8')
        except Exception:
            return obj
    else:
        return obj

def try_decode_markdown_blocks(text):
    def decode_block(match):
        content = match.group(1)
        try:
            return "```" + content.encode('latin1').decode('utf-8') + "```"
        except Exception:
            return "```" + content + "```"
    # 只处理 ```...``` 里的内容
    return re.sub(r"```([\s\S]*?)```", decode_block, text)

# 发送SSE请求，收集所有data:消息，保留原始和格式化内容
def send_message(question, conversation_id):
    payload = {
        "question": question,
        "conversationId": conversation_id
    }
    headers = {}
    if BEARER_TOKEN:
        headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    messages = []
    with requests.post(API_URL, json=payload, headers=headers, stream=True, timeout=30) as resp:
        resp.raise_for_status()
        for line in resp.iter_lines():  # 不用decode_unicode，手动解码
            if line:
                try:
                    line = line.decode('utf-8')
                except Exception:
                    line = line.decode('latin1')
                if line.startswith("data:"):
                    data = line[5:].strip()
                    if data and data != "[DONE]":
                        # 尝试格式化JSON
                        try:
                            obj = json.loads(data)
                            obj = decode_obj(obj)
                            pretty = json.dumps(obj, ensure_ascii=False, indent=2)
                            messages.append({"raw": data, "pretty": pretty})
                        except Exception:
                            messages.append({"raw": data, "pretty": data})
    return messages

def main():
    groups = read_questions("questions.csv")
    results = []
    for group, qas in groups.items():
        conversation_id = str(uuid.uuid4())
        for idx, qa in enumerate(qas):
            print(f"Group {group} Q{idx+1}: {qa['question']}")
            try:
                sse_messages = send_message(qa['question'], conversation_id)
            except Exception as e:
                sse_messages = [{"raw": f"请求失败: {e}", "pretty": f"请求失败: {e}"}]
            # 拼接所有事件内容
            all_data_raw = "\n\n".join([msg["raw"] for msg in sse_messages])
            all_data_pretty = "\n\n".join([msg["pretty"] for msg in sse_messages])
            all_data_pretty = try_decode_markdown_blocks(all_data_pretty)
            results.append({
                "group": group,
                "question": qa['question'],
                "expected_answer": qa['answer'],
                "data_raw": all_data_raw,
                "data_pretty": all_data_pretty
            })
            time.sleep(1)  # 避免请求过快
    # 保存结果
    with open("results.csv", "w", newline='', encoding='utf-8') as csvfile:
        fieldnames = ["group", "question", "expected_answer", "data_raw", "data_pretty"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    print("测试完成，结果已保存到 results.csv")

if __name__ == "__main__":
    main()
