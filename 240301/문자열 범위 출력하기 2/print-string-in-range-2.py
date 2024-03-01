arr=input()
a=int(input())

if a>len(arr):
    print(arr)
else:
    for i in arr[-1:-12:-1]:
        print(i,end='')