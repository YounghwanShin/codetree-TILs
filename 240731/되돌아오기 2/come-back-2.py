dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
dir_map = {"L":3, "R":1}
direction = 3
x, y = 0, 0
time = 0

arr=list(input())

for message in arr:
    if message == "L" or message == "R":
        time +=1
        direction = (direction + dir_map[message])%4
        continue

    x, y = x + dxs[direction], y + dys[direction]
    time += 1

    if x == 0 and y == 0:
        print(time)
        break
else:
    print(-1)