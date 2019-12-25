import random

yeni_kelime = ""


def f(kelime):
    global yeni_kelime
    if len(kelime) == 0:
        pass
    else:
        sec = random.choice(kelime)
        yeni_kelime += sec
        kelime = kelime.replace(sec, "", 1)
        return f(kelime)


def siklik_bul(kelime):
    a = []
    for i in kelime:
        if kelime.count(i) > 1:
            a.append(kelime.count(i))
            kelime = kelime.replace(i, "")
    return a



f("merhaba")

tekrar = siklik_bul("Büyükharfler")
print(yeni_kelime)
print(tekrar)
# emhabar