a,b=map(int, input().split())

val=str(a+b)
cnt=0

for char in val:
    if char=='1':
        cnt+=1

print(cnt)