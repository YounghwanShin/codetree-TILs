n=int(input())

arr=list(map(int, input().split()))

min_index,min_val=arr.index(min(arr)),min(arr)

arr=arr[min_index::]

max_val=max(arr)

if max_val<=min_val:
    print(0)
else:
    print(max_val-min_val)