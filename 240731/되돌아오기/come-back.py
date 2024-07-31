N=int(input())
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
dir_map = {"E":0, "S":1, "W":2, "N":3}
x, y = 0, 0
time = 0
val=False

for _ in range(N):
    temp = input().split()
    dir_num = dir_map[temp[0]]
    size = int(temp[1])

    for _ in range(1,size+1):
        x, y = x + dxs[dir_num], y + dys[dir_num]
        time += 1
        if x==0 and y==0:
            val = True
            break
    if val == True:
        print(time)
        break

if val==False:
    print(-1)