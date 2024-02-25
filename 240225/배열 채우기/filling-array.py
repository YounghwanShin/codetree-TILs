arr=list(map(int,input().split()))
arr_2=[]

for i in arr:
    if i==0:
        break
    arr_2.append(i)

for k in arr_2[::-1]:
    print(k, end=' ')