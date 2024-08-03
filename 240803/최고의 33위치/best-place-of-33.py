N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def count_coin(row_s, row_e, col_s, col_e):
    return sum(arr[r][c] for r in range(row_s, row_e + 1) for c in range(col_s, col_e + 1))

max_val = 0

for i in range(N - 2): 
    for k in range(N - 2):  
        current_val = count_coin(i, i + 2, k, k + 2)  
        max_val = max(max_val, current_val)

print(max_val)