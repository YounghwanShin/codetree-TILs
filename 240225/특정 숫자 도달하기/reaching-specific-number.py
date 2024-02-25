arr = list(map(int, input().split()))

cnt, n = 0, 0

for i, num in enumerate(arr):
    if num >= 250:
        break
    cnt += num
    n = i + 1

print(cnt, f'{cnt/n:.1f}' if n else 0)