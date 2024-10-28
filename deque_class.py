class Deque:
    def __init__(self):
        self.__deque = ["elemen", 12, 3, 4]

    def __str__(self):
        return f'Valores internos del deque: {self.__deque}'

    def add_first(self, item):
        self.__deque.insert(0, item)

    def remove_first(self):
        return None if len(self.__deque) == 0 else self.__deque.pop(0)

    def add_last(self, item):
        self.__deque.append(item)

    def remove_last(self):
        return None if len(self.__deque) == 0 else self.__deque.pop()

deque1 = Deque()
deque1.add_first("hola")
deque1.add_last("2")
deque1.remove_last()
deque1.remove_first()
print(deque1)