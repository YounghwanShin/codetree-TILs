def palindrome(A):
    return A == A[::-1]

A = input()
if palindrome(A):
    print('Yes')
else:
    print('No')