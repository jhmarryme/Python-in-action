# 搜索引擎基类
class SearchEngineBase:
    def __init__(self):
        print('父类初始化')

    def add_corpus(self, file_path):
        with open(file_path, "r") as fin:
            text = fin.read()
            self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception("process_corpus未定义")

    def search(self, query):
        raise Exception("search未定义")


# 分词的搜索引擎
import re


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_word = {}

    def process_corpus(self, id, text):
        self.__id_to_word[id] = self.parse_text_to_word(text)

    def search(self, query):
        query_words = self.parse_text_to_word(query)
        results = []
        for id, words in self.__id_to_word.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results

    @staticmethod
    def parse_text_to_word(text):
        # 使用正则表达式去除标点和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的set
        return set(word_list)

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True


def main(search_engine):
    for file_path in ['txt/1.txt', 'txt/2.txt', 'txt/3.txt', 'txt/4.txt', 'txt/5.txt']:
        search_engine.add_corpus(file_path)
    while True:
        query = input('请输入检索词，按q结束')
        if query == 'q':
            break
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


if __name__ == '__main__':
    bow_engine = BOWEngine()
    main(bow_engine)
