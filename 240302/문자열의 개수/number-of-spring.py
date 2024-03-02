A=input()
cnt=1
arr=[]

while A!='0':
    if cnt%2!=0:
        arr.append(A)
    cnt+=1
    A=input()

print(cnt-1)
print(*arr,sep='\n')