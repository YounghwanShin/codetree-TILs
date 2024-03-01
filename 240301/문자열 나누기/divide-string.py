n=int(input())
arr=list(map(str, input().split()))

new_num=''.join(arr)

for i in range(len(new_num)):
    if (i+1)%5==0:
        print(new_num[i])
    else:
        print(new_num[i],end='')