arr = list(map(int, input().split()))

i = 0
while len(arr) < 10:
    arr.append(2*arr[i] + arr[i+1])
    i+=1

print(*arr, end=' ')