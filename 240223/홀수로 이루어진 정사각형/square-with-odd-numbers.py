n=int(input())

for i in range(11,10+n*2,2):
    for j in range(0,n):
        print(i+2*j, end=' ')
    print()