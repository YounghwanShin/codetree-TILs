def f(n):
    if n==1:
        return 0
    elif n%2==0:
        return f(n/2)+1
    else:
        return f(n//3)+1

N=int(input())
print(f(N))