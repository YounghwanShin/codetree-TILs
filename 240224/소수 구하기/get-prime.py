import math

n= int(input())

resurt_arr=[]

for i in range(2,n+1):
    prime = True
    for j in range(2, math.isqrt(i) + 1):
        if i % j == 0:
            print=False
    if prime == True:
        print(i, end=' ')