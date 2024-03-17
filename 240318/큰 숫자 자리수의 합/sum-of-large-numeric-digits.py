def g(n):
    if n<10:
        return n
    
    return g(n//10)+(n%10)

def f(num):
    val=1
    for i in num:
        val*=i
    return g(val)

num=map(int,input().split())
print(f(num))