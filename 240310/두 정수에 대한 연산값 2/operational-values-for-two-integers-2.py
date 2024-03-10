a,b=(map(int,input().split()))

def f(a,b):
    if a>b:
        a,b=a*2,b+10
    else:
        a,b=a+10,b*2
    return a,b

print(*f(a,b))