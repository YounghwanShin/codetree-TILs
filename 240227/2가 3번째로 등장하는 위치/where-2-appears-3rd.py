n=int(input())

arr=list(map(int, input().split()))

n=0

for i,num in enumerate(arr):
    if num==2:
        n+=1
    if n==3:
        print(i+1)
        break