"""
Bir dize verildiğinde, tüm benzersiz karakterlerin karşılaştırıldığından emin olun.
Örneğin, 'abcde' dizgisi tüm benzersiz karakterlere sahiptir ve True döndürmelidir.
'Aabcde' dizgisi yinelenen karakterler içeriyor ve false döndürmeli.
"""
def uni_char(st):

    if len(st) > 256:
        return False

    char_set = [False]*128

    for i in range(0, len(st)):

         val = ord(st[i])

         if char_set[val]:
             return False

         char_set[val] = True

    return True

if __name__ == '__main__':
    st = "abcde"
    st1 = "Aabcdee"
    print(uni_char(st))
    print(uni_char(st1))




