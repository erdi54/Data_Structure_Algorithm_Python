class Node:
    def __init__(self, data, position=0):
       self . data = data
       self . next = None


class Linked_list:

    def __init__(self):
         self.head = None

    #Listenin başına yeni düğüm eklme
    def per_push(self, new_data):

        new_node = Node(new_data)  # yeni düğüm oluştur
        new_node.next = self.head #yeni düğüm işaretçisi bağlı listenin başını göster
        self.head = new_node  # listenin başını yeni düğümü ata

    #listenin sonuna eleman ekleme
    def end_push(self,new_data):

        new_node = Node(new_data)
        if self.head is None: # Eğer bağlı liste boş ise yeni düğümü ekle ve yeni düğüm listenin başı olur
            self.head =new_node
        # Dolaştırıcı oluştur ve listenin başını başlangıç olarak ata
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # istenilen  bir düğümü başka bir düğümden sonra ekleme
    def insert_after_item(self, prev_node, new_data):

        if prev_node is None:
            print("Sonrasına eklemek istediğiniz eleman bulunamadı")
            return
        new_node = Node(new_data)
        # yeni düğümün işaretçisini sonrasına eklemek istediğimiz düğümün işaretçisine ata
        new_node.next = prev_node.next
        # sonrasına eklemek istediğimiz düğümün işarettçisi yeni düğümü göster
        prev_node.next = new_node

    # istenilen  bir düğümü başka bir düğümden önce ekleme
    def insert_before_item(self, prev_node, new_data):

        if self.head is None:
            print("Listede eleman yok")
            return
        if prev_node == self.head.data:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == prev_node:
                break
            temp = temp.next
        if temp.next is None:
            print("Liste içinde veri yok")
        else:
            new_node = Node(new_data)
            new_node.next = temp.next
            temp.next = new_node

    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 1
        temp = self.head
        while i < index - 1 and temp is not None:
            temp = temp.next
            i = i + 1
        if temp is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

    #Baştan Düğüm silme
    def delete_at_start(self):
        if self.head is None:
            print("Bu listede silinecek element yok")
            return
        self.head = self.head.next

    # sondan  düğüm silme
    def delete_at_end(self):
        if self.head is None:
            print("Listede silinecek öğe yok")
            return
        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # istenilen aradan düğüm silme
    def delete_node_by_position(self, position):

        if self.head == None:
            return
        temp = self.head

        # Başın çıkarılması gerekiyorsa
        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Silinecek düğümün önceki düğümünü bulun
        for i in range(position -1):
            temp = temp.next
            if temp is None:
                break

        # Konum, düğüm sayısından fazlaysa
        if temp is None:
            return
        if temp.next is None:
            return

        # Düğüm temp.next silinecek düğümdür
        # store pointer silinecek düğümün bir sonrakine
        next = temp.next.next
        temp.next = None
        temp.next = next


    # düğüm arama
    def search(self,node):
        if self.head is None:
            print("Listede eleman yok !!")
            return
        temp =self.head
        while temp != None:
            if temp.data == node:
                print("Item found")
                return True
            temp = temp.next
        print("item not found")
        return False

    #liste üzerindeki tüm düğümleri yazdırma
    def iter_loop(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        return temp

    #Düğüm sayısını döndürme
    def countList(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count



if __name__ == '__main__':
    l_list = Linked_list()
    l_list.head = Node(10)
    e1 = Node(20)
    e2 = Node(30)
    # Link first Node to second node
    l_list.head.next = e1
    # Link second Node to third  node
    e1.next = e2
    print("Listenin Başına yeni liste ekleme:", l_list.per_push(3))
    #///////////////////////////////////////
    for i in range(1, 4):
       l_list.end_push(i*20)
    # ///////////////////////////////////////
    l_list.insert_at_index(5, 15)
    l_list.delete_at_start()
    # ///////////////////////////////////////
    l_list.insert_before_item(30, 9)
    print("Araya Düğüm ekleme:", l_list.insert_after_item(l_list.head.next, 80))
    print("/////////////////////////////////")
    print("Liste üzerindeki düğümler:")
    l_list.iter_loop()
    print("/////////////////////////////////")
    print("Listenin Eleman sayısı:",l_list.countList())
    print("/////////////////////////////////")
    print("Bağlı Listede Eleman arama:", l_list.search(40))
    l_list.delete_at_end()
    l_list.delete_at_start()
    l_list.delete_node_by_position(4)
    l_list.iter_loop()

