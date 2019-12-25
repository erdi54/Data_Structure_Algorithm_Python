import random

class CircularQueue:

    class Node:
        __slots__ = ["_element", "_next"]

        def __init__(self, element, next):
            self._element = element
            self. _next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            return False

        head = self._tail._next
        return head. _element

    def dequeue(self):
        if self.is_empty():
            return False

        oldhead = self._tail._next

        if self._size == 1:
            self._tail = None

        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, data):
        newest = self.Node(data, None)

        if self.is_empty():
            newest._next = newest

        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next



if __name__ == '__main__':
    cl_list = CircularQueue()
    list = []
    for i in range(0, 10):
       x = random.randint(1, 100)
       cl_list.enqueue(x)
       list.append(x)
    print(list)
    print("Listenin Başı:", cl_list.first())
    print(cl_list.rotate())

    for i in range(0, 10):
        print(cl_list.dequeue())