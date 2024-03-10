N=int(input())
arr=list(map(int, input().split()))

def absolute(n,A):
    for i in range(n):
        if A[i]<=0:
            A[i]=-A[i]

absolute(N,arr)
print(*arr)