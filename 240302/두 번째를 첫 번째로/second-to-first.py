A=list(input())

a=A[0]
b=A[1]

for i in range(len(A)):
    if A[i]==b:
        A[i]=a

print(''.join(A))