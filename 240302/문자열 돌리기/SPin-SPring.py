A=input()
L=len(A)

for _ in range(L+1):
    print(A)
    A = A[-1]+ A[:-1]