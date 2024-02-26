arr = list(map(int, input().split()))

cnt = 0

for i, num in enumerate(arr):
    if num == 0:
        break
    cnt += num

print(cnt)