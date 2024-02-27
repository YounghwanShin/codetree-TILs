n=int(input())

arr=list(map(int, input().split()))

min_val=arr[0]

for i in arr[1:]:
    if min_val>i:
        min_val=i

print(min_val,arr.count(min_val))