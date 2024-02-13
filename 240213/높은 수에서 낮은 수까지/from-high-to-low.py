a,b = map(int, input().split())

if a>=b:
    for i in (a,b-1,-1):
        print(i, end=" ")
else:
    for i in (b,a-1,-1):
        print(i, end=" ")