n=int(input())

satisfied=True

if n!=1:
    for i in range(2,n):
        if n%i==0:
            satisfied=False
else:
    satisfied=False

if satisfied==True:
    print('N')
else:
    print('C')