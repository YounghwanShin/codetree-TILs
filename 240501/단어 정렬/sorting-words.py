n=int(input())
arr=[]
for _ in range(n):
    arr.append(input())

arr.sort()

print('\n'.join(arr))