arr_2d=[input() for _ in range(10)]
a=input()

cnt=False

for arr in arr_2d:
    if arr[-1]==a:
        print(arr)
        cnt=True

if cnt==False:
    print('None')