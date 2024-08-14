# 抽象函数和抽象类
from abc import ABCMeta, abstractmethod


# 也可以直接继承ABC类
class Entity2(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document4(Entity2):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


if __name__ == '__main__':
    document = Document4()
    document.set_title("hp")
    print(document.get_title())
