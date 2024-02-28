arr_2=[list(map(int, input().split())) for _ in range(2)]

for arr in arr_2:
    print(f'{sum(arr)/len(arr):.1f}',end=' ')
print()

for j in range(4):
    sum_val=0
    for i in range(2):
        sum_val+=arr_2[i][j]
    print(f'{sum_val/2:.1f}', end=' ')
print()

sum_val_2=0
for k in range(2):
    sum_val_2+=sum(arr_2[k])
print(f'{sum_val_2/8:.1f}')