import math

start, end = map(int, input().split())

n=0

for i in range(start, end+1):
    divisor_num = 1
    for j in range(2, math.isqrt(i) + 1):
        if i % j == 0:
            if j == (i // j):
                divisor_num += 1
            else:
                divisor_num += 2
    if divisor_num==3:
        n+=1

print(n)