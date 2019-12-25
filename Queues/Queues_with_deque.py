
from collections import deque

# Bir kuyrugu başlatma
q = deque()

# Kuyruktan çıkan elemanlar
q.append('a')
q.append('b')
q.append('c')

print("Başlangıçta Kuyruk")
print(q)

# Removing elements from a queue
print("\nKuyruktan kaldırılmış öğeler")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nÖğeleri kaldırdıktan sonra sıra")
print(q)