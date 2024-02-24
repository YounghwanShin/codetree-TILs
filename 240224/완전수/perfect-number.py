import math

start, end = map(int, input().split())

n=0

for i in range(start, end+1):
    divisor_sum = 1
    for j in range(2, math.isqrt(i) + 1):
        if i % j == 0:
            if j == (i // j):
                divisor_sum += j
            else:
                divisor_sum += j + (i // j)
    if divisor_sum==i:
        n+=1

print(n)