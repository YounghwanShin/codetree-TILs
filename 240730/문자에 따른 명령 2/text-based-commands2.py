x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]  # 동남서북
dic = {"L": 3, "R": 1}
num = 3

arr = list(input())

for command in arr:
    if command == "F":
        x += dx[num]
        y += dy[num]
    else:
        num = (num + dic[command]) % 4

print(x, y)