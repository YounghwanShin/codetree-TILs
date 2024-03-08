def cal_1(n):
    val=True

    for i in range(2,n):
        if n%i==0:
            val=False
    return val

def cal_2(n):
    arr=str(n)
    hap=0

    for k in arr:
        hap+=int(k)

    if hap%2==0:
        return True
    else:
        return False

a,b=map(int, input().split())
cnt=0

for i in range(a,b+1):
    if cal_1(i) and cal_2(i):
        cnt+=1

print(cnt)