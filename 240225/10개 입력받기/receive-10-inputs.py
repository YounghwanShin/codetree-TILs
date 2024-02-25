arr = list(map(int, input().split()))

zero_index = arr.index(0) if 0 in arr else len(arr)

sum_arr=sum(arr[:zero_index])
ave_arr=sum_arr/zero_index

print(sum_arr, f'{ave_arr:.1f}')