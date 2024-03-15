def pprint(n):
    if n==0:
        return

    pprint(n-1)
    print('HelloWorld')

N=int(input())
pprint(N)