a,b= map(int, input().split())
cnt=0

for i in range(2, 10, 2): 
    for j in range(b, a-1, -1):
        cnt+=1
        print(f"{j} * {i} = {i * j}", end="")
        if cnt <= b-a:
            print(" /", end=" ")
    cnt=0
    print()