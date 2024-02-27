N_1,N_2 = map(int, input().split())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

try:
    index_arr_B_1 = arr_A.index(arr_B[0])
    if arr_A[index_arr_B_1:index_arr_B_1+len(arr_B)] == arr_B:
        print('Yes')
    else:
        print('No')
except ValueError:
    print('No')