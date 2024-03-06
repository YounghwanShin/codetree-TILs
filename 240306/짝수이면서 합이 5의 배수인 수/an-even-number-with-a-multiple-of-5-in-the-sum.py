def comparison(n):
    arr_n=str(n)
    if n%2==0 and (int(arr_n[0])+int(arr_n[1]))%5==0:
        print('Yes')
    else:
        print('No')

n=int(input())

comparison(n)