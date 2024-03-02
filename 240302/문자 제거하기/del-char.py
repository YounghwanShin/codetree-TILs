A=list(input())

while len(A)>1:
    a=int(input())
    if a>len(A)-1:
        A.pop()
    else:
        A.pop(a)
    print(''.join(A))