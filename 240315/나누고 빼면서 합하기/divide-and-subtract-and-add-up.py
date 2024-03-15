def calculate(m):
    if m%2!=0:
        m-=1
    else:
        m/=2
    return int(m)

n,m=map(int,input().split())
A=list(map(int,input().split()))

sum_val=0

while m!=1:
    sum_val+=A[m-1]
    m=calculate(m)

sum_val+=A[0]

print(sum_val)