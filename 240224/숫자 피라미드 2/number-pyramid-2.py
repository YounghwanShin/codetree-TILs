n=int(input())

cnt=0

for i in range(1,n+1):
    for _ in range(i):
        cnt+=1
        print(cnt, end=' ')
    print()