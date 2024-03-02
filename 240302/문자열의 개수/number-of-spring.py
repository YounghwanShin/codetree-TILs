arr = []
A = input()

while A != '0':
    if len(arr) % 2 == 0:
        arr.append(A)
    A = input()

print(len(arr) * 2 - 1)
print(*arr, sep='\n')