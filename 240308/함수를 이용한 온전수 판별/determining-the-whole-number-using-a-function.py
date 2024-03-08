def on(n):
    arr=str(n)
    val=True
    if n%2==0 or (n%3==0 and n%9!=0):
        val=False
    elif int(arr[-1])==5:
        val=False
    return val

a,b=map(int, input().split())
cnt=0

for i in range(a,b+1):
    if on(i):
        cnt+=1

print(cnt)