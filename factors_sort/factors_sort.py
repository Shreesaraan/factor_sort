import math
def factor(num):
    count = 0
    if num == 0 or num == 1:
        return 1
    sr = math.sqrt(num)
    for i in range(1, int(sr) + 1):
        if num % i == 0:
            count += 2
            if i == sr:
                count -= 1
    return count

def factor_sort(array):
    array.sort(key=lambda num:(factor(num),num)) 
    return array

array=list(map(int,input("Enter the Array Elements : ").split()))
print(factor_sort(array))