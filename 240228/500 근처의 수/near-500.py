arr=list(map(int, input().split()))

max_val,min_val=0,1001

for num in arr:
    if max_val<num and num<500:
        max_val=num
    if min_val>num and num>500:
        min_val=num
    
print(max_val,min_val)