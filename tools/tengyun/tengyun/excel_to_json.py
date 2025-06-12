import pandas as pd


def excel_to_json(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path)
    ## 看看列名
    columns = df.columns.tolist()
    json_objects = []
    print(df.columns.tolist())
    for index, row in df.iterrows():
        json_object = {
            'index': row.iloc[0],
            'question': row.iloc[1],
            'standard_answer': row.iloc[2],  # 第一列
            'user_answer': row.iloc[3],  # 第二列
            'cosine': '',
            'score': '',
            'score_details': ''
        }
        json_objects.append(json_object)
    return json_objects


# 示例用法
if __name__ == "__main__":
    excel_file = 'todo.xlsx'  # 替换成你的Excel文件路径
    json_data = excel_to_json(excel_file)
