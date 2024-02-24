n=int(input())

cnt=64

for i in range(1,n+1):
    for j in range(1,n+1):
        if i>j:
            print(' ', end=' ')
        else:
            cnt+=1
            print(chr(cnt),end=' ')
            if cnt==90:
                cnt=64
    print()