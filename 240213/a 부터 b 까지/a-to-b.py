a,b=map(int, input().split())

while a<=b:
    print(a)
    if a%2==0:
        print(a, end=" ")
        a+=3
    else:
        print(a, end=" ")
        a*=2