arr = list(map(int, input().split()))

for num in arr:
    if num == 0:
        break
    print(num // 2 if num % 2 == 0 else num + 3, end=' ')