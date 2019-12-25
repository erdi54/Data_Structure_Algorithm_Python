import random

class _DoublyLinkedBase:
    class _Node:
         __slots__ = ['_element', '_prev', '_next']

         def __init__(self, element, prev, next):
             self._element = element
             self._prev = prev
             self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_between(self, data, prev_node, next_node):
        # Mevcut iki düğüm arasına öğe veri ekleyin ve yeni düğümü döndürün.
        new_node = self._Node(data, prev_node, next_node)
        prev_node._next = new_node
        next_node._prev = new_node
        self._size += 1
        return new_node

    def delete_node(self, node):
        prev_node = node._prev
        next_node = node._next
        prev_node._next = next_node
        next_node._next =prev_node
        self._size -= 1
        # silinen öğe kayıt
        element = node._element
        # kullanım dışı düğüm
        node._prev = node._next = node._element = None
        # silinen elemanı döndür
        return element

    def printList(self):
        list = []
        temp = self._header
        while temp is not None:
            list.append(temp._element)
            temp = temp._next
        return list


class LinkedDeque(_DoublyLinkedBase):

    def first(self):

        if self.is_empty():
            return False #Çift uçlu kuyruk boş
        return self._header._next._element

    def last(self):
        if self.is_empty():
            return False  # Çift uçlu kuyruk boş
        return self._trailer._prev._element

    def insert_first(self, data):
        self.insert_between(data, self._header, self._header._next)

    def insert_last(self, data):
        self.insert_between(data ,self._trailer._prev, self._trailer)

    def delete_last(self):
       """ Elemanı sökün ve deque'nin önünden geri getirin. Deque boşsa Boş istisnayı kaldır."""

       if self.is_empty():
           return False  # Çift uçlu kuyruk boş

       return self.delete_node(self._trailer._prev)


    def delete_first(self):

        if self.is_empty():
           return False # Çift uçlu kuyruk boş

        return self.delete_node(self._header._next)


if __name__ == '__main__':
    dlList = LinkedDeque()

    for i in range(0,10):
        x = random.randint(1, 100)
        dlList.insert_first(x)

    for j in range(0,10):
        y = random.randint(1, 100)
        dlList.insert_last(y)

    print(dlList.printList())
    print(dlList.first())
    print(dlList.delete_first())
    print(dlList.printList())
    print(dlList.delete_last())
    print(dlList.printList())
    print(dlList.last())
    print(dlList.first())






