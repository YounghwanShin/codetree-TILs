A,q=input().split()

def one(A):
    return A[1:]+A[0]

def two(A):
    return A[-1]+A[:-1]

def three(A):
    return A[::-1]

for _ in range(int(q)):
    k=int(input())
    if k==1:
        A=one(A)
        print(A)
    elif k==2:
        A=two(A)
        print(A)
    elif k==3:
        A=three(A)
        print(A)