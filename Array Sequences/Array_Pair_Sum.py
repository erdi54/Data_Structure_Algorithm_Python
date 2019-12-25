"""
Bir tamsayı dizilimi verildiğinde, k * değerine karşılık gelen tüm * * unique ** çiftlerini verir.

"""
def pair_sum(arr,k):
    counter = 0
    lookup = set()
    for num in arr:
        if k-num in lookup:
            counter += 1
        else:
            lookup.add(num)
    return counter
    pass

print(pair_sum([1,3,2,5],4))