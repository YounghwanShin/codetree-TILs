n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
B.sort()

def is_equal():
    for a,b in zip(A,B):
        if a!=b:
            return 'No'
    else:
        return 'Yes'

print(is_equal())