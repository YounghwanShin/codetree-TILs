n_1,n_2=map(int, input().split())
A=input().split()
B=input().split()

def arr(a,b,A,B):
    for i in range(a-b+1):
        for k in range(b):
            cnt=0
            if A[i+k]==B[k]:
                cnt+=1
            if cnt==b:
               return True
    return False

if arr(n_1,n_2,A,B):
    print('Yes')
else:
    print('No')