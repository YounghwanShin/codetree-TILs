A=input()

arr=[]
cnt=1

for i in range(len(A)):
    if i+1==len(A):
        if A[i]==A[i-1]:
            arr.append((A[i],cnt))
        else:
            arr.append((A[i],1))
    else:
        if A[i]==A[i+1]:
            cnt+=1
        else:
            arr.append((A[i],cnt))
            cnt=1

words=''

for k,num in arr:
    words=words+k+str(num)

print(len(words))
print(words)