n=int(input())
arr=list(map(int, input().split()))

min_val = arr[0]
max_diff = 0

for i in range(1, n):
    if arr[i] < min_val:
        min_val = arr[i]
    else:
        max_diff = max(max_diff, arr[i] - min_val)

print(max_diff)