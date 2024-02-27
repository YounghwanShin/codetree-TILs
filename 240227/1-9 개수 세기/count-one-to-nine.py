n=int(input())

arr = list(map(int, input().split()))

max_val = max(arr)
count_arr = [0] * (max_val+1)

for elem in arr:
    count_arr[elem-1] += 1

for i in range(max_val + 1):
    cnt = count_arr[i]
    print(f"{cnt}")