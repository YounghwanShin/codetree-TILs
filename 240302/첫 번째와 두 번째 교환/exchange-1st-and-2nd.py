A=list(input())

a,b=A[0],A[1]

for i in range(len(A)):
    if A[i]==a:
        A[i]=b
    elif A[i]==b:
        A[i]=a

print(''.join(A))