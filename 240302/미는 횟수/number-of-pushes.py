A=input()
B=input()

def transfer(arr):
    return arr[-1]+arr[:-1]

for i in range(len(A)):
    if A==B:
        print(i)
        break
    A=transfer(A)
else:
    if A==B:
        print(i)
    else:
        print(-1)