def print_max_index_until_one(n, arr):
    max_index = arr.index(max(arr))

    if max_index == 1:
        print(max_index + 1)
        return
    
    while max_index > 1:
        print(max_index + 1, end=' ')
        arr = arr[:max_index]
        max_index = arr.index(max(arr))

    print(1)

n = int(input())
arr = list(map(int, input().split()))
print_max_index_until_one(n, arr)