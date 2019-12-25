import random

class CircularLinkedList:

    class Node:
        __slots__ = ["_data", "_next"]

        def __init__(self, data, next=None):
            self._data = data
            self._next = next

    def __init__(self):
        self.head = None


    def push(self, data):
        new_node = self.Node(data)
        temp = self.head

        new_node._next = self.head

        if self.head is not None:
            while temp._next != self.head:
                temp = temp._next
            temp._next = new_node

        else:
            new_node._next = new_node

        self.head = new_node


    def printList(self):
        list = []
        temp = self.head
        if self.head is not None:
            while True:
                list.append(temp._data)
                temp = temp._next
                if temp == self.head:
                    break
            return list

if __name__ == '__main__':

    cl_list = CircularLinkedList()

    for i in range(0, 10):
        x = random.randint(1, 100)
        cl_list.push(x)

    print(cl_list.printList())
