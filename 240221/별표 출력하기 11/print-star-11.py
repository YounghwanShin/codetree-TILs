n=int(input())+3

for i in range(1,n+2):
    if i%2==0:
        for k in range(1,n+2):
            if k%2==0:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()
    else:
        for _ in range(n+1):
            print('*', end=' ')
        print()