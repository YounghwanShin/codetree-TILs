def plaindrome(A):
    n=len(A)
    if A[:n//2]==A[n:n//2:-1]:
        return True
    return False

A=input()
if plaindrome(A):
    print('Yes')
else:
    print('No')