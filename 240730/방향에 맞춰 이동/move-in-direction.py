N=int(input())
x, y = 0,0

dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

dic={'W':0,'S':1,'N':2,'E':3}

for _ in range(N):
    a,b=input().split()
    b=int(b)
    x,y=x+dx[dic[a]]*b, y+dy[dic[a]]*b

print(x,y)