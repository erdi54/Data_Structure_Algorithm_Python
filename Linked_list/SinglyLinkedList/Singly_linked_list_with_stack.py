import random

class LinkedStack:
    class _Node:
        __slots__ = ['_element', '_next']

        def __init__(self, element, next):

            self._element = element
            self._next = next

    def __init__(self):
        self. _head = None
        self. _size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head) # Stack olduğundan eklenen elemanı sürekli olarak eklenen elemanı baş düğüm yapıyor
        self. _size += 1  # Boyutu sürekli artırıyor

    def top(self):
        if self.is_empty():
            return False

        return self._head._element

    def pop(self):
        if self.is_empty():
            return False

        answer = self._head._element # Baş elemanı dondürüyor
        self._head = self._head._next  # Baş elemanı Bir sonraki elemana atıyor
        self._size -= 1  # Boyutu azaltıyor
        return answer  # Listeden atılan elemanı dödürüyor


if __name__ == '__main__':

    S = LinkedStack()
    list = []
    for i in range(0,10):
        x = random.randint(1, 100)
        S.push(x)
        list.append(S.top())
    print(list)
    print(S.is_empty())

    for i in range(0, len(list)):
        print("Cıkan Eleman: ", S.top())
        S.pop()

    print(S.is_empty())





