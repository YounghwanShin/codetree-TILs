arr = list(map(int, input().split()))

zero_index = arr.index(0) if 0 in arr else len(arr)


for num in arr[zero_index-1::-1]:
    print(num, end=' ')