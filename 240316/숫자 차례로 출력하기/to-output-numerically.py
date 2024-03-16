def f(N,M):
    if N==0:
        return
    print(M-N,end=' ')
    f(N-1,M)

def g(N):
    if N==0:
        return
    print(N,end=' ')
    g(N-1)

N=int(input())
f(N,N+1)
print()
g(N)