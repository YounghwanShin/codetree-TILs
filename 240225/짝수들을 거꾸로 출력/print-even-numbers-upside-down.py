n=int(input())
arr = [i for i in map(int, input().split()) if i % 2 == 0]
print(*arr[::-1], end=' ')