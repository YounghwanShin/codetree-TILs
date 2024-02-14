a,b=map(int,input().split())

def calculate(a,b):
    val_sum=0
    for i in range(a,b+1):
        if i%5==0:
            val_sum+=i
    return val_sum

if a<b:
    print(calculate(a,b))
elif a>b:
    print(calculate(b,a))
else:
    if a%5==0:
        print(a)