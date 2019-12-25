"""
AAAABBBBCCCCCDDEEEE' biçiminde bir dize verildiğinde, onu 'A4B4C5D2E4' olacak şekilde sıkıştırın.
Bu sorun için, yanlış bir şekilde tek veya çift harfli dizeleri "sıkıştırabilirsiniz".
Örneğin, teknik olarak daha fazla yer kaplasa da, 'AAB'nin' A2B1'i geri getirmesi tamam.
İşlev ayrıca büyük / küçük harf duyarlı olmalıdır, böylece 'AAAaaa' dizgisi 'A3a3' değerini döndürür.
"""

def compress(string):
    temp = {}

    result = " "

    for x in string:
        if x in temp:
            temp[x] = temp[x] + 1
        else:
            temp[x] = 1

    for key, value in temp.items():
        result += str(key) + str(value)

    return result

if __name__ == '__main__':
    string = "AAAABBBBCCCCCDDEEEE"
    str = compress(string)
    print(str)