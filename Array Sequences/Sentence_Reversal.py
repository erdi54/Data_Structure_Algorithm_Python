"""
Bir kelime dizisi verilen tüm kelimeleri tersten uygulayın. Örneğin:

Verilen:

'Bu en iyisi'
Dönüş:

'en iyisi bu'
Bu alıştırmanın bir parçası olarak tüm önde gelen ve sondaki boşlukları kaldırmalısınız. Böylece bu gibi girişler:

'uzay burada' ve 'burada boşluk'
her ikisi de:

'burada uzay'

"""


def reverseWords(input):

    # boşlukla ayrılmış dizgenin sözcüklerini böl
    inputWords = input.split(" ")

    # kelimelerin ters listesi
    # varsayalım ki öğeler listemiz var = [1,2,3,4],
    # list [0] = 1, liste [1] = 2 ve dizin -1
    # son eleman listesi [-1] = 4 ([3] = 4 listesine eşdeğer)
    # Yani, inputWords [-1 :: - 1] burada üç argüman var
    # ilk -1, yani son elemandan başla demek
    # ikinci argüman boş, listenin sonuna taşın
    # üçüncü argümanlar adımların farkıdır
    inputWords = inputWords[-1::-1]

    # şimdi kelimeleri boşlukla birleştir
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(reverseWords(input) )