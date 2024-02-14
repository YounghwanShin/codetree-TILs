import math

n = int(input())
val_sum = 1  

for i in range(2, math.isqrt(n) + 1):
    if n % i == 0:
        if i == (n // i):
            val_sum += i
        else:
            val_sum += i + (n // i)

if val_sum == n:
    print("P")
else:
    print("N")