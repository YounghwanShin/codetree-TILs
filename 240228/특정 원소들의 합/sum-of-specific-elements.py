arr_2=[list(map(int, input().split())) for _ in range(4)]

sum=0

for i in range(4):
    for j in range(4):
        if i>=j:
            sum+=arr_2[i][j]

print(sum)