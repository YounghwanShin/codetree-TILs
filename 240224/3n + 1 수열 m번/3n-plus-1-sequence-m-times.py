m=int(input())

def calculation(k):
    n=0
    while k!=1:
        if k%2==0:
            k/=2
        else:
            k=(k*3)+1
        n+=1
    return n

for _ in range(m):
    q = int(input())
    print(calculation(q))