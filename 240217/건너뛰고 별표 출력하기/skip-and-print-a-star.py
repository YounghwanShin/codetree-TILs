n=int(input())

for i in range(1,n+1):
    for _ in range(i):
        print('*', end="")
    print("\n")
for k in range(n-1,0,-1):
    for _ in range(k):
        print('*', end="")
    print("\n")