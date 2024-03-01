arr=input()
a=int(input())

if a>len(arr):
    print(arr[::-1])
else:
    for i in arr[-1:-a-1:-1]:
        print(i,end='')