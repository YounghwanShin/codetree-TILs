def f(n,cnt):
    if n==1:
        return cnt
    elif n%2==0:
        cnt+=1
        return f(n/2,cnt)
    else:
        cnt+=1
        return f(n//3,cnt)

N=int(input())
print(f(N,cnt=0))