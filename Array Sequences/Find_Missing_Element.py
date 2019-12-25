"""
Negatif olmayan bir tam sayı dizisini göz önünde bulundurun. İlk dizinin öğelerinin karıştırılması ve rastgele bir öğenin silinmesi ile ikinci bir dizi oluşturulur.
Bu iki dizi göz önüne alındığında, ikinci dizide hangi öğenin eksik olduğunu bulun.

İşte bir örnek giriş, ilk dizi karıştırılır ve ikinci diziyi oluşturmak için 5 sayısı kaldırılır.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:

5 is the missing number

"""

def finder(arr1,arr2):

    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            print("missing", arr1[i])
    for j in range(len(arr2)):
        if arr2[j] not in arr1:
            print("added", arr2[j])



arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(set(arr1).difference(arr2))
print(finder(arr1,arr2))