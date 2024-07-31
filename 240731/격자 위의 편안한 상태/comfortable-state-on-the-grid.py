N,M = map(int, input().split())

arr = [[0] * N for _ in range(N)]

drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

def is_comfortable(r,c):
    cnt = 0
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and arr[nr][nc] == 1:
            cnt += 1
    return 1 if cnt==3 else 0

for _ in range(M):
    r,c = map(int, input().split())
    r,c= r-1, c-1
    arr[r][c] = 1
    print(is_comfortable(r,c))