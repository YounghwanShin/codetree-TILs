n=int(input())

for i in range(n,0,-1): 
    for _ in range(n-i):
        print(" ", end=" ")
    for _ in range(1,(2*i)):
        print("*", end=" ")
    print()
for i in range(2,n+1): 
    for _ in range(n-i):
        print(" ", end=" ")
    for j in range(1,(2*i)):
        print("*", end=" ")
    print()