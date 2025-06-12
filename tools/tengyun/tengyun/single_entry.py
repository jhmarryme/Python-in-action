import json

from todo.tengyun.call_ernie import call_ernie
from todo.tengyun.excel_to_json import excel_to_json
from todo.tengyun.json_to_excel import json_to_excel
from todo.tengyun.similarity import calculate_similarity


# 分段处理json
def call(content):
    result = call_ernie(content)
    result = result.replace("```json", "")
    result = result.replace("```", "")
    return json.loads(result)


if __name__ == '__main__':
    prompt = """
    对我给出的json串进行分析, 其中question为问题,
        1. 将standard_answer作为标准答案, 对user_answer进行打分(满分为100分), 记录分数和评分的详情, 将结果回填到score和score_details字段中
        2. 最终相应给我json串, 不需要你的计算过程, 不要包含markdown语法, 不要多余的解释
        3. 请记住只需要返回给我json串, 其他任何额外信息都不要有
    json串如下: \n
    """
    # 读取excel为json
    excel_file = '1.xlsx'  # 替换成你的Excel文件路径
    json_data = excel_to_json(excel_file)
    json_data = json_data[4:7]
    excel_json_objects = []
    for item in json_data:
        try:
            print(item.__str__())
            data = call(prompt + item.__str__())
            data['cosine'] = str(calculate_similarity(data['standard_answer'], data['user_answer']))
            excel_json_objects.append(data)
        except Exception as e:  # Catch any exceptions
            print(f"Error processing item: {item}. Exception: {e}")

    json_to_excel(excel_json_objects)
