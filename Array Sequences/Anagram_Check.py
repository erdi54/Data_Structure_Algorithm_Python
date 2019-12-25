"""
İki karakter verildiğinde anagram olup olmadıklarını kontrol edin.
 Anagram, iki dizenin aynı harfleri kullanarak yazılabildiği zamandır
(bu nedenle harfleri farklı bir ifade veya sözcük elde etmek için yeniden düzenleyebilirsiniz).

"""

def check(s1, s2):

    if (sorted(s1) == sorted(s2)):
       return True
    else:
       return False

s1 = "listen"
s2 = "silent"

print(check(s1, s2))

str="Hayat Kısa Python Oğrenin"
x=[i for i in str if i.isupper()]
print(x)

