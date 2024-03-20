def T(n):
    if n==1:
        return 2
    elif n==2:
        return 4
    return (T(n-1)*T(n-2))%100

n=int(input())
print(T(n))