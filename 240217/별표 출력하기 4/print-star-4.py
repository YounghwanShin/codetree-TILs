n=int(input())

for k in range(n,0,-1):
    for _ in range(k):
        print('*', end=" ")
    print()
for i in range(2,n+1):
    for _ in range(i):
        print('*', end=" ")
    print()