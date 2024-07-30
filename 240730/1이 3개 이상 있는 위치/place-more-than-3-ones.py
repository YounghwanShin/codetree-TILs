n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

k = 0

for x in range(n):
    for y in range(n):
        cnt = 0

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n) and arr[nx][ny] == 1:
                cnt += 1
        
        if cnt >= 3:
            k += 1

print(k)