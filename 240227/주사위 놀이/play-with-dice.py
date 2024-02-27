arr = list(map(int, input().split()))

count_arr = [0]*6

for elem in arr:
    count_arr[elem-1] += 1

for i in range(6):
    cnt = count_arr[i]
    print(f"{i+1} - {cnt}")