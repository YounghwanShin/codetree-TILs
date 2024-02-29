n,m=map(int, input().split())

arr_2=  [
        [0 for _ in range(m)]
        for _ in range(n)    
        ]

cnt=0

for j in range(m):
    if j%2==0:
        for i in range(n):
            arr_2[i][j]=cnt
            cnt+=1
    else:
        for i in range(n-1,-1,-1):
            arr_2[i][j]=cnt
            cnt+=1

for i in range(n):
    for j in range(m):
        print(arr_2[i][j], end=' ')
    print()