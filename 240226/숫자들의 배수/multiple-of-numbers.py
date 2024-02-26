n = int(input())

arr = [n]
val = 0
i = 0

while True:
    print(arr[i], end=' ')
    if arr[i] % 5 == 0:
        val += 1
    if val == 2:
        break
    arr.append(arr[i] + n)
    i += 1