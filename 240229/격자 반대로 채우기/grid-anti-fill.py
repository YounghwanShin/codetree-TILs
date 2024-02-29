n=int(input())

arr_2=  [
        [0 for _ in range(n)]
        for _ in range(n)    
        ]

cnt=1

for j in range(n):
    if j%2==0:
        for i in range(n):
            arr_2[n-i-1][n-j-1]=cnt
            cnt+=1
    else:
        for i in range(n-1,-1,-1):
            arr_2[n-i-1][n-j-1]=cnt
            cnt+=1

for i in range(n):
    for j in range(n):
        print(arr_2[i][j], end=' ')
    print()