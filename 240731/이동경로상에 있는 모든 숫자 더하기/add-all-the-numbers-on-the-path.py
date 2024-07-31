drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
dir_map = {"L": 3, "R": 1} 
direction = 3  

N, T = map(int, input().split())
dir_arr = list(input())
arr = [list(map(int, input().split())) for _ in range(N)]

r, c = N//2, N//2

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

val = arr[r][c]

for message in dir_arr:
    if message in dir_map:
        direction = (direction + dir_map[message]) % 4
    else:
        nr, nc = r + drs[direction], c + dcs[direction]
        if in_range(nr, nc):
            r, c = nr, nc
            val += arr[r][c]

print(val)