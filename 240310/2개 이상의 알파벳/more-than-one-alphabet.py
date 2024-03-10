A=input()

def f(A):
    for i in range(len(A)-1):
        if A[i]!=A[i+1]:
            return True
    return False

if f(A):
    print('Yes')
else:
    print('No')