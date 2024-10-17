import pandas as pd

# 读取 CSV 文件
file_path = 'quiz.csv'  # 替换为你的文件路径
df = pd.read_csv(file_path)


# 定义一个函数来格式化每一行
def optimized_format_row(row):
    # 获取问题内容
    question = '\nquestion:\n' + row['question'] + '\n'

    # 收集非空的选项
    options = []
    if pd.notna(row['option_a']):
        options.append(f"选项A：{row['option_a']}")
    if pd.notna(row['option_b']):
        options.append(f"选项B：{row['option_b']}")
    if pd.notna(row['option_c']):
        options.append(f"选项C：{row['option_c']}")
    if pd.notna(row['option_d']):
        options.append(f"选项D：{row['option_d']}")
    if pd.notna(row['option_e']):
        options.append(f"选项E：{row['option_e']}")

    # 如果有选项存在，格式化选项内容
    options_text = "\nanswer:\n**问题选项**\n" + "\n".join(options) if options else ""

    # 转换 verified 列，1 为"已验证"，否则为"未验证"
    verification_status = "**已验证**" if row['verified'] == 1 else "**未验证**"
    if row['verified'] != 1:
        verification_status +=f"\n正确次数: {row['right_count']}\n" + f"错误次数: {row['wrong_count']}"

    # 格式化答案和额外信息
    answer = (
        f"{options_text}\n"
        f"\n**题目序号**: {row['id']}\n"
        f"\n**问题答案**：**{row['answer']}**\n"
        f"\n**该题是否经过验证**: {verification_status}\n"
    )

    return question + answer


# 对每一行应用格式化函数
optimized_formatted_data = df.apply(optimized_format_row, axis=1)

# 创建一个新的 DataFrame，包含格式化后的问题和答案
optimized_df = pd.DataFrame(optimized_formatted_data.tolist(), columns=['分段内容'])

# 保存生成的新 CSV 文件
output_file = 'optimized_formatted_quiz_2.csv'  # 替换为你想保存的文件路径
optimized_df.to_csv(output_file, index=False)

print(f"解析后的 CSV 文件已保存为: {output_file}")
