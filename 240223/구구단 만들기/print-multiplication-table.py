a,b= map(int, input().split())
cnt=0

for i in range(1, 10): 
    for j in range(b, a-1, -2):
        cnt+=1
        print(f"{j} * {i} = {i * j}", end="")
        if cnt <= (b-a)//2:
            print(" /", end=" ")
    cnt=0
    print()