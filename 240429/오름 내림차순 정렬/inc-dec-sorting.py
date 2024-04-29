n=int(input())
arr=list(map(int, input().split()))

sorted_list=sorted(arr)
reversed_list=list(reversed(sorted(arr)))

print(*sorted_list)
print(*reversed_list)