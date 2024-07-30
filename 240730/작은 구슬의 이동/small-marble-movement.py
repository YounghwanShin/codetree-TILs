n, t = map(int, input().split())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

mapper = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3
}

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

r, c, d = input().split()
x, y = int(r) - 1, int(c) - 1

move_dir = mapper[d]

for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(nx, ny):
        move_dir = (move_dir + 2) % 4
        continue
    
    x, y = nx, ny

print(x + 1, y + 1)