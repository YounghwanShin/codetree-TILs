def f(N):
    if N==0:
        return 0
    
    return f(N-1)+N

N=int(input())
print(f(N))