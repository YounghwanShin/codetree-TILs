a,b=map(int, input().split())
cnt=0
def one(n):
    if n==1:
        return 0
    for k in range(2,n):
        if n%k==0:
            return 0
    return n

for i in range(a,b+1):
    cnt+=one(i)

print(cnt)