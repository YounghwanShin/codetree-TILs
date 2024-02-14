n = int(input())

A=B=C=0

for i in range(1,n+1):
    if i%12==0:
        C+=1
    elif i%3==0:
        B+=1
    elif i%2==0:
        A+=1

print(A,B,C)