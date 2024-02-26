arr=list(map(int, input().split()))

zero_index = [i for i, k in enumerate(arr) if k == 0]

cnt=0

for i in range(zero_index[0]-3 : zero_index[0]):
    cnt+=arr[i]

print(cnt)