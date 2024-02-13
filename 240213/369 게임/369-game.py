n = int(input())

for i in range(1, n+1):
    n_arr=list(str(i))
    if i>=10:
        if int(n_arr[0])in [3,6,9] or int(n_arr[1])in [3,6,9]:
            print(0, end=" ")
        elif i%3==0:
            print(0, end=" ")
        else:
            print(i, end=" ")
    else:
        if i%3==0:
            print(0, end=" ")
        else:
            print(i, end=" ")