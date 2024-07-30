"""
        Y                (x, y + 1)
        ^                    ^
        |                    | 3
        |              2     |      0
        | (x - 1, y) <------ (x, y) -----> (x + 1, y)
        |                    | 1
        |                    v
        |                (x, y - 1)
        |
---------------------------------------------> X
"""

n, t = map(int, input().split())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

mapper = {
    'L': 0,  
    'D': 1,  
    'R': 2,  
    'U': 3   
}

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

arr = input().split()
x, y = int(arr[1]) - 1, int(arr[0]) - 1 
c_dir = arr[2]

move_dir = mapper[c_dir]

for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(nx, ny):
        move_dir = (move_dir + 2) % 4
        continue 
    
    x, y = nx, ny

print(y + 1, x + 1)