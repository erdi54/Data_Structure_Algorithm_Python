
str = "cümledeki kelimeleri büyük harfle başlatma"
dizi = str.split(" ")


for i in range(len(dizi)):

   if dizi[i][0].islower():
         dizi[i] = dizi[i].capitalize()


output = ' '.join(dizi)

print(output)