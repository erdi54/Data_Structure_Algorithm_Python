"""
Dinamik Dizi Egzersizi
Bu alıştırmada kendi Dinamik Dizi sınıfımızı oluşturacağız!

"""
import ctypes

class DynamicArray (object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
       # Dizide sıralanmış öğelerin döndürme sayısı
        return self.n

    def __getitem__(self, item):
        if not 0 <= item <= self.n:
            return IndexError('İtem sınırların dışında')

        return self.A[item]

    def make_array(self, new_cap):
       # yeni kapasitesi verilen bir dizi döndürür
        return (new_cap * ctypes.py_object)()

    def _resize(self, new_cap):
        # Dahili diziyi new_cap kapasitesine göre yeniden boyutlandır

        B = self.make_array(new_cap) # Yeni büyük dizi

        #Mevcut tüm değerlere referans
        for i in range(self.n):
            B[i] = self.A[i]

        # A'yı yeni büyük dizi olarak adlandır
        self.A = B
        self.capacity = new_cap

    def append(self, item):
        # diziye eleman ekleme
        if self.n == self.capacity:
            # eğer yeteri kadar yer yoksa çift kapasite tanımlama
            self._resize(2*self.capacity)
        self.A[self.n] = item
        self.n += 1

if __name__ == "__main__":

    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    print(arr)
    print(len(arr))
    print(arr[0])
    print(arr[1])




