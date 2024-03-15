def hap(a,b):
    global A
    return sum(A[a-1:b])

n,m=map(int,input().split())
A=list(map(int,input().split()))

for _ in range(m):
    a1,a2=map(int,input().split())
    print(hap(a1,a2))