N_1,N_2 = map(int, input().split())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr_index=[arr_A.index(i) for i in arr_A if i==arr_B[0]]
k=True

try:
    for j in arr_index:
        if arr_A[j:j+len(arr_B)] == arr_B:
            k=True
            break
        else:
            k=False
except ValueError:
    print('No')

if k==True:
    print('Yes')
else:
    print('No')