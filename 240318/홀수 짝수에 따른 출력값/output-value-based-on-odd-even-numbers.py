def f(n):
    if n==1 or n==2:
        return n

    return f(n-2)+n

n=int(input())
print(f(n))