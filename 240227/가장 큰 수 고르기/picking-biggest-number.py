arr=list(map(int,input().split()))

max_value=arr[0]

for i in arr[1:]:
    if max_value<i:
        max_value=i

print(max_value)