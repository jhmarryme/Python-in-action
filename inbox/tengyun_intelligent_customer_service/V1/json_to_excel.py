import pandas as pd

def json_to_excel(data):
    """
    将JSON数据转换为Excel文件

    Args:
    - data (list of dicts): 包含JSON数据的列表，每个字典代表一条数据
    - excel_filename (str): 要保存的Excel文件名

    Returns:
    - None
    """
    # 将JSON数据转换为DataFrame
    df = pd.DataFrame(data)

    excel_filename = 'answers.xlsx'
    # 将DataFrame保存为Excel文件
    df.to_excel(excel_filename, index=False, engine='openpyxl')

    print(f"Excel文件保存成功: {excel_filename}")
