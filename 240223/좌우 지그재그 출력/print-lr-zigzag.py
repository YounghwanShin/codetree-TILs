n=int(input())

cnt=1

for i in range(1,n+1):
    if i%2!=0:
        for _ in range(n):
            print(cnt, end=' ')
            cnt+=1
        print()
    else:
        cnt+=n-1
        for _ in range(n):
            print(cnt, end=' ')
            cnt-=1
        cnt=cnt+n+1
        print()