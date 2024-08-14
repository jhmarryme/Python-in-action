# 类的继承
class Entity():
    def __init__(self, object_type):
        print("父类构造函数")
        self.object_type = object_type

    def get_contex_length(self):
        raise Exception("没有定义get_context_length")

    def print_title(self):
        print(self.title)


class Document3(Entity):
    def __init__(self, title, author, context):
        Entity.__init__(self, "document")
        print("Document3调用初始函数!")
        self.title = title
        self.author = author
        self.__context = context

    def get_context_length(self):
        return len(self.__context)


class Video(Entity):
    def __init__(self, title, author, video_length):
        Entity.__init__(self, "video")
        print("video调用初始函数!")
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length

if __name__ == '__main__':
    # 类继承
    hp_book = Document3("a", "aa", "aaa")
    hp_movie = Video("b", "bb", 30)

    print(hp_book.object_type)
    print(hp_movie.object_type)
    hp_book.print_title()
    hp_movie.print_title()
    print(hp_book.get_context_length())
    print(hp_movie.get_context_length())