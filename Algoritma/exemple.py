import random


def kelimeyi_karistir(kelime):
    global yeni_kelime
    if len(kelime) == 0:
        pass
    else:
        sec = random.choice(kelime)
        yeni_kelime += sec
        kelime = kelime.replace(sec, "", 1)
        return kelimeyi_karistir(kelime)


def kelime_uzunlugu_faktoriyel(kelime):
    sonuc = 1
    uzunluk = len(kelime)
    while uzunluk > 1:
        sonuc *= uzunluk
        uzunluk -= 1
    return sonuc


def faktoriyel(n):
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc


def tekrar_eden_harfleri_bul(kelime):
    a = []
    for i in kelime:
        if kelime.count(i) > 1:
            a.append(kelime.count(i))
            kelime = kelime.replace(i , "")
    sonuc = 1
    for i in a:
        sonuc *= faktoriyel(i)
    return sonuc


a = set()

while True:
    yeni_kelime = ""
    kelime = "abi"
    kelimeyi_karistir(kelime)
    if len(a) != kelime_uzunlugu_faktoriyel(kelime) / \
        tekrar_eden_harfleri_bul(kelime):
        a.add(yeni_kelime)
    else:
        break

print(a)
