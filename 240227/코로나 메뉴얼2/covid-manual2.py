def calculate(YN, temp):
    if temp>=37 and YN=='Y':
        return 'A'
    elif temp>=37 and YN=='N':
        return 'B'
    elif YN=='Y':
        return 'C'
    else:
        return 'D'

count_arr={'A':0, 'B':0, 'C':0, 'D':0}

for _ in range(3):
    a,b=input().split()
    elem=calculate(a, int(b))
    count_arr[elem]+=1

for i in count_arr.keys():
    print(count_arr[i], end=' ')

if count_arr['A']==2:
    print('E')