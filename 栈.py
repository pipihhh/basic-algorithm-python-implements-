class Stack(object):
    def __init__(self, count):
        self.__count = count
        self.__content = [None for _ in range(count)]
        self._cursor = 0

    @property
    def is_empty(self):
        return self._cursor == 0

    @property
    def is_full(self):
        return self._cursor == self.__count

    def peek(self):
        return self.__content[self._cursor-1]

    def push(self, item):
        self.__content[self._cursor] = item
        self._cursor += 1

    def pop(self):
        if self.is_empty:
            raise IndexError("栈为空")
        self._cursor -= 1
        return self.__content[self._cursor]


stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.pop())
