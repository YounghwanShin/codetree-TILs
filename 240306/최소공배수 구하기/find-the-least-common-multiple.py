n,m=map(int,input().split())

def val(n,m):
    key=n*m
    while m>0:
        i=m
        n,m=i,n%m
    return int(key/n)

print(val(n,m))