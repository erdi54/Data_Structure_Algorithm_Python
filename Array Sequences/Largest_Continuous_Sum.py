"""
Bir tamsayı dizisi verildiğinde (pozitif ve negatif) en büyük sürekli toplamı bulun.

"""

def large_cont_sum (arr, size):
    if len(arr) == 0:
        return 0

    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, size):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

if __name__ == "__main__":
    arr = [1,2,-1,3,4,10,10,-10,-1]
    print(large_cont_sum(arr, len(arr)))
    a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print(large_cont_sum(a,len(a)))


