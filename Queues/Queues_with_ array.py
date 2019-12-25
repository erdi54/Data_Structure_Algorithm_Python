
# Bir kuyruğu başlatma
queue = []

# Kuyruğa eleman eklendi
queue.append('a')
queue.append('b')
queue.append('c')

print("Başlangıçta Kuyruk")
print(queue)

# Kuyruktan çıkan elemanlar
print("\nKuyruktan kaldırılmış öğeler")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nÖğeleri kaldırdıktan sonra sıra")
print(queue)