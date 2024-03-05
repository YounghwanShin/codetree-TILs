def val(n,m):
    while m>0:
        i=m
        n,m=i,n%m
    return n

n,m=map(int, input().split())
print(val(n,m))