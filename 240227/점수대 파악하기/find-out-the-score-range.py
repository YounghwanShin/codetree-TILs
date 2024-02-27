arr = list(map(int, input().split()))

count_arr=[0]*10

for elem in arr:
    if elem==0:
        break
    if elem//10!=0:
        count_arr[(elem//10)-1]+=1

for i,cnt in enumerate(count_arr[::-1]):
    print(f'{(10-i)*10} - {cnt}')