"""
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn pandas
"""
import csv


def log_action(action, row_index, details):
    """记录每次操作"""
    with open("cleaning_log.txt", "a") as log_file:
        log_file.write(f"{action} on row {row_index}: {details}\n")


def clean_csv(input_file, output_file, log_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
            open(output_file, mode='w', newline='', encoding='utf-8') as outfile, \
            open(log_file, mode='w', newline='', encoding='utf-8') as log:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # 获取预期的列数
        header = next(reader)
        expected_columns = len(header)
        writer.writerow(header)
        log.write(f"Header written: {header}\n")

        for row_number, row in enumerate(reader, start=2):  # 从2开始，因为1是header
            # 如果列数不匹配，处理该行
            if len(row) != expected_columns:
                if len(row) > expected_columns:
                    # 如果多列，则记录并修复
                    log.write(f"Row {row_number}: Extra columns found, trimming. Original row: {row}\n")
                    row = row[:expected_columns]
                else:
                    # 如果少列，可以选择删除该行，或者尝试修复
                    log.write(f"Row {row_number}: Missing columns, row will be deleted. Original row: {row}\n")
                    continue  # 删除该行

            writer.writerow(row)

    print(f"Cleaning complete. Output saved to '{output_file}' and log saved to '{log_file}'.")


# 读取CSV文件
if __name__ == '__main__':
    input_csv = 'data.csv'
    output_csv = 'cleaned_output.csv'
    log_file = 'cleaning_log.txt'

    clean_csv(input_csv, output_csv, log_file)
