n = int(input())
arr_2d = [
    [1 for _ in range(i+1)]
    for i in range(n)
]

for i in range(1,n):
    for j in range(1,i):
        arr_2d[i][j]=arr_2d[i-1][j-1]+arr_2d[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(arr_2d[i][j], end=' ')
    print()