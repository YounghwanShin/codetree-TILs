n=int(input())

arr_2d=[input() for _ in range(n)]

cnt=0
len_arr=0

for arr in arr_2d:
    for i in arr:
        if i=='a':
            cnt+=1
    len_arr+=len(arr)

print(len_arr,cnt)