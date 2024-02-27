arr=list(map(int, input().split()))

min_val=arr[0]
max_val=arr[0]

for i in arr[1:]:
    if i==999 or i==-999:
        break
    else:
        if min_val>i:
            min_val=i
        if max_val<i:
            max_val=i

print(max_val,min_val)