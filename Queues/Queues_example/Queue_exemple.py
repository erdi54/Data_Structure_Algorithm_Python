"""
Kuyruk Yöntemleri ve Nitelikleri

Kendi kuyruğumuzu uygulamaya başlamadan önce, sahip olacağı özniteliği ve yöntemleri gözden geçirelim:

* Kuyruk () boş olan yeni bir kuyruk oluşturur. Hiçbir parametreye ihtiyaç duymaz ve boş bir sıra döndürür.
* enqueue (öğe) kuyruğun arkasına yeni bir öğe ekler. Öğeye ihtiyacı var ve hiçbir şey döndürmüyor.
* dequeue () ön öğeyi kuyruktan kaldırır. Hiçbir parametreye ihtiyaç duymaz ve öğeyi döndürür. Kuyruk değiştirildi.
* isEmpty (), sıranın boş olup olmadığını test eder. Hiçbir parametreye ihtiyaç duymaz ve bir boolean değeri döndürür.
* size () kuyruktaki öğe sayısını döndürür. Hiçbir parametreye ihtiyaç duymaz ve bir tamsayı döndürür.
Bir Queue sınıfının uygulanması istenmesi çok yaygındır! Sınıf aşağıdakileri yapabilmelidir:

"""
import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
         if self.items is None :
             return True

         else:
             return False

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print(self):
        list = []
        for i in range(0, len(self.items)):
           list.append(self.items[i])
        return list

if __name__ == '__main__':
   q = Queue()
   for i in range(0,10):
       x = random.randint(0, 100)
       q.enqueue(x)
   del i

   print("Kuruktaki Elemanlar ve sırası:",q.print())

   print(q.isEmpty())
   print("Kuyruk Boyutu",q.size())

   for i in range(0,10):
       print("Kuyruktan çıkan elman ",q.dequeue())
   del i
   print("Kuyruk Boyutu",q.size())
