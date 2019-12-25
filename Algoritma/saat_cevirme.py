
saniye = int(input ("saniye sayısını girin:"))
saat = saniye // 3600
saniye = saniye % 3600
dakika = saniye // 60
saniye = saniye % 60
print (saat, ":", sep = "", end = "")
onlar = dakika//10
birler = dakika % 10
print(onlar, birler, ":", sep = "", end = "")
onlar = saniye // 10
birler = saniye % 10
print (onlar, birler, sep = "")