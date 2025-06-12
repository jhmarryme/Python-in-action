def main(arg1: list, query: str) -> dict:
    num_results = len(arg1)
    output = f"# 检索到 {num_results} 个结果如下：\n"
    arg1.reverse()
    for i, result in enumerate(arg1, 1):
        content = result.get("content", "无内容")
        if query and query in content:
            content = content.replace(query, f"**{query}**")
        output += f"# ------结果 {i}------:\n{content}\n\n"

    if num_results > 1:
        output += "\n**！！！该题目存在多个相似结果，请仔细分辨！！！**\n"

    return {
        "result": output,
    }

if __name__ == '__main__':
    query = '结果'
    arg1 = [
        {'content': '结果1'},
        {'content': '结果2'}
    ]
    print(main(arg1))
