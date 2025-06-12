import os

import pandas as pd


def split_csv_to_folder(input_file, output_dir, chunksize=15):
    """
    将CSV文件分割成多个小的CSV文件，并存放到指定文件夹中

    Args:
      input_file: 输入CSV文件的路径
      output_dir: 输出文件夹的路径
      chunksize: 每个输出文件包含的行数
    """

    df = pd.read_csv(input_file, chunksize=chunksize)

    # 创建输出文件夹，如果不存在
    os.makedirs(output_dir, exist_ok=True)

    for i, chunk in enumerate(df):
        # 构造输出文件名
        output_file = os.path.join(output_dir, f"chunk_{i}.csv")
        # 将数据块写入CSV文件
        chunk.to_csv(output_file, index=False)


if __name__ == '__main__':
    # 示例用法
    input_file = "data.csv"
    output_dir = "output_folders"
    split_csv_to_folder(input_file, output_dir)
