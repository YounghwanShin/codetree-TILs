n,m=map(int, input().split())

arr=[[0 for _ in range(m)] for _ in range(n)]

cnt=1

if n==1:
    for j in range(m):
        arr[0][j]=cnt
        cnt+=1
elif m==1:
    for i in range(n):
        arr[i][n]=cnt
        cnt+=1
else:
    for j in range(m):
        i=0
        while j>=0:
            arr[i][j]=cnt
            cnt+=1
            i,j=i+1,j-1
    else:
        if m>1:
            for i in range(1,n):
                j=m-1
                while i<n:
                    arr[i][j]=cnt
                    cnt+=1
                    i,j=i+1,j-1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()