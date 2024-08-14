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


# 简单的搜索引擎
class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super().__init__()
        print("子类初始化")
        self.id_to_texts = {}

    def process_corpus(self, id, text):
        self.id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.id_to_texts.items():
            if query in text:
                results.append(id)
        return results


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
    simple_engine = SimpleEngine()
    main(simple_engine)
