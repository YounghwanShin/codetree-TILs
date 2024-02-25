arr = list(map(int, input().split()))

try:
    zero_index = arr.index(0)
except ValueError:
    zero_index = len(arr)

for num in arr[zero_index-1::-1]:
    print(num, end=' ')