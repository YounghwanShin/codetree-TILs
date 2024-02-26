arr = list(map(int, input().split()))

for i, num in enumerate(arr):
    arr.append((arr[i]+arr[i+1])%10)
    if len(arr)==10:
        break

print(*arr, end=' ')