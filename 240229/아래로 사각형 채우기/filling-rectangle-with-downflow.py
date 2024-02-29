n=int(input())

arr_2=  [
        [0 for _ in range(n)]
        for _ in range(n)    
        ]

cnt=1

for j in range(n):
    for i in range(n):
        arr_2[i][j]=cnt
        cnt+=1

for i in range(n):
    for j in range(n):
        print(arr_2[i][j], end=' ')
    print()