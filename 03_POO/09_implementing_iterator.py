"""
    Implement iterator protocol

    Idea: Rebuild Python List
"""

class MyList:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, value):
        self.__items.append(value)

    def __getitem__(self, index):
        return self.__items[index]

    def __seitem__(self, index, value):
        if index >= len(self.__items):
            self.__items.append(value)
        self.__items[index] = value

    def __delitem__(self, index):
        del self.__items[index]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    list = MyList()
    list.add('Luiz')
    list.add('Mary')

    # list = list(list)

    # print(list)
    # list[0] = 'John'
    # list[2] = 'Does it work?'

    # del list[2]

    # print(list)

    for value in list:
        print(value)

    print(list)