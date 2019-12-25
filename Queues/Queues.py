import random as rand

class Queuen():
    def __init__(self):
        self.entries =[]
        self.lenght = 0
        self.front = 0

    def insert(self, item):
        self.entries.append(item)
        self.lenght = self.lenght+1

    def remove(self):
        if self.lenght > 0:
          item = self.entries[0]
          self.lenght = self.lenght-1
          del self.entries[0]
          return item

        else:
            print("Kuyruk Boş")

    def front(self):
        return self.lenght

    def size(self):
        return int(self.lenght)

    def show(self):
        print(self.entries)

if __name__ == '__main__':
    q1 = Queuen()
    for i in range(0,10):
        x = rand.randint(1,100)
        q1.insert(x)

    q1.show()
    print(q1.remove())
    print(q1.size())
    q1.show()
    for j in range(10):
        print("Eleman Kuyruktan Çıkarıldı:", q1.remove())

