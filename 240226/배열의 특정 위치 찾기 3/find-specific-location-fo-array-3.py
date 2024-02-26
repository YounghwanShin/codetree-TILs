arr = list(map(int, input().split()))

first_zero_index = next((i for i, k in enumerate(arr) if k == 0), -1)

cnt = sum(arr[first_zero_index-3:first_zero_index]) if first_zero_index >= 3 else 0

print(cnt)