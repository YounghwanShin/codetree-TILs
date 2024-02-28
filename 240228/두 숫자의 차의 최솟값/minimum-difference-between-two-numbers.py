import sys

n=int(input())
arr=list(map(int, input().split()))

min_diff=sys.maxsize

for i in range(1,n):
    min_diff=min(min_diff,arr[i]-arr[i-1])

print(min_diff)