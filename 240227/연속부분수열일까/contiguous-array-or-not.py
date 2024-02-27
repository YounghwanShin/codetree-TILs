N_1, N_2 = map(int, input().split())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

start_indices = [i for i, x in enumerate(arr_A) if x == arr_B[0]]

for start in start_indices:
    if arr_A[start:start+len(arr_B)] == arr_B:
        print('Yes')
        break
    else:
        print('No')