arr = list(map(int, input().split()))

try:
    zero_index = arr.index(0)
except ValueError:
    zero_index = len(arr)

sum_arr=sum(arr[:zero_index])
ave_arr=sum_arr/zero_index

print(sum_arr, f'{ave_arr:.1f}')