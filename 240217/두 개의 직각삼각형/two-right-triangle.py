n=int(input())

for i in range(n,0,-1):
    for _ in range(i):
        print('*',end='')
    for _ in range(2*(n-i)):
        print(' ',end="")
    for _ in range(i):
        print('*',end='')
    print()