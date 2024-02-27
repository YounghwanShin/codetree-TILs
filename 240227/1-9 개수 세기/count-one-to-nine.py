n=int(input())

arr = list(map(int, input().split()))

count_arr = [0] *9

for elem in arr:
    count_arr[elem-1] += 1

for i in range(9):
    cnt = count_arr[i]
    print(f"{cnt}")