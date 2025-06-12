import pandas as pd
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(text1, text2):
    # 分词
    texts = [" ".join(jieba.lcut(text1)), " ".join(jieba.lcut(text2))]

    # 使用TF-IDF向量化
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    # 计算余弦相似度
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return cosine_sim[0][0]

def process_excel(file_path, output_path):
    # 读取Excel文件
    df = pd.read_excel(file_path)
    print(df.columns.tolist())
    # 假设第一列和第二列的列名分别为 "Column1" 和 "Column2"
    df['相似度'] = df.apply(lambda row: calculate_similarity(row['A'], row['B']), axis=1)

    # 如果相似度低于0.8，则在第四列添加标记
    df['标记'] = df['相似度'].apply(lambda x: 'X' if x < 0.8 else '')

    # 将结果写回到新的Excel文件
    df.to_excel(output_path, index=False)

# 调用函数处理Excel文件
input_file_path = 'input1.xlsx'  # 输入文件路径
output_file_path = 'output.xlsx'  # 输出文件路径
process_excel(input_file_path, output_file_path)
