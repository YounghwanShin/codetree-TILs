n=int(input())

arr=list(map(int, input().split()))

for i in range(len(arr)) :
    max_index = i
    for j in range(i+1, len(arr)) :
        if arr[max_index] < arr[j] :
            max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]


print(arr[0],arr[1])