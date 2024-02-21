n=2*int(input())+1

for i in range(1,n+1):
    if i%2==0:
        for k in range(1,n+1):
            if k%2==0:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()
    else:
        for _ in range(n):
            print('*', end=' ')
        print()