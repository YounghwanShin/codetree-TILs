arr = list(map(int, input().split()))

zero_index = arr.index(0) if 0 in arr else len(arr)

cnt,n=0,0

for i in arr[0:zero_index]:
    if i%2==0:
        cnt+=i
        n+=1

print(n,cnt)