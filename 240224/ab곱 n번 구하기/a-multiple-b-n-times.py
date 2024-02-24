n=int(input())

def calculate(Q,W):
    product=1
    for i in range(Q,W+1):
        product*=i
    return product

for _ in range(n):
    a,b=map(int, input().split())
    print(calculate(a,b))