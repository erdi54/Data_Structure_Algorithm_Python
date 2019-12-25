import random

import random

class LinkedStack:
    class _Node:
        __slots__ = ['_element', '_next']

        def __init__(self, element, next):

            self._element = element
            self._next = next

    def __init__(self):
        self. _head = None
        self._tail = 0
        self. _size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            return False
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            return False

        answer = self._head._element  # Baş elemanı dondürüyor
        self._head = self._head._next  # Baş elemanı Bir sonraki elemana atıyor
        self._size -= 1  # Boyutu azaltıyor
        if self.is_empty():
            self._tail = None
        return answer  # Listeden atılan elemanı dödürüyor

    def enqueue(self, e):
        newest = self._Node(e, None)

        if self.is_empty():
            self._head = newest  # Liste boş ise yeni düğümü başa atanır
        else:
            self._tail._next = newest # Liste boş değil ise yeni düğümü sona atanır

        self._tail = newest  # yeni düğüm sona eklenir
        self._size += 1  # boyut arttırılır

if __name__ == '__main__':
    S = LinkedStack()
    list = []
    for i in range(0, 10):
        x = random.randint(1, 100)
        S.enqueue(x)
        list.append(x)
    print(list)
    print(S.is_empty())
    print(S.first())
    for i in range(0, len(list)):
        print("Cıkan Eleman: ", S.first())
        S.dequeue()

    print(S.is_empty())