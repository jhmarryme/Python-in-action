from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import jieba

def cosine_similarity_text(str1, str2):
    words1 = ' '.join(chinese_tokenizer(str1))
    words2 = ' '.join(chinese_tokenizer(str2))
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([words1, words2])
    return cosine_similarity(tfidf)[0][1]

def chinese_tokenizer(text):
    return jieba.cut(text, cut_all=False)

# 计算文本相似度
text1 = "您好，电子行程单是“电子发票 (航空运输电子客票行程单)”的简称，是现纸质“航空运输电子客票行程单”的电子化替代，是全面数字化的电子发票（简称数电票）的一种。"
text2 = "电子行程单是航空运输电子客票行程单的电子化替代，是一种全面数字化的电子发票。"

similarity = cosine_similarity_text(text1, text2)
print(similarity)