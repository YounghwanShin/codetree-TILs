a,b=map(int, input().split())
cnt=0

def one(n):
    arr=['3','6','9']
    list_n=str(n)
    for i in arr:
        if i in list_n:
            return True

def two(n):
    global cnt
    if n%3==0 or one(n):
        cnt+=1

for k in range(a,b+1):
    two(k)

print(cnt)