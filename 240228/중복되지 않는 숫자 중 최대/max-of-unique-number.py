def find_largest_unique_number(n, arr):
    arr.sort(reverse=True)

    if arr[0] != arr[1]:
        return arr[0]

    for i in range(1, n-1):
        if arr[i] != arr[i+1] and arr[i-1] != arr[i]:
            return arr[i]

    if arr[-2] != arr[-1]:
        return arr[-1]
        
    return -1

n = int(input())
arr = list(map(int, input().split()))
print(find_largest_unique_number(n, arr))