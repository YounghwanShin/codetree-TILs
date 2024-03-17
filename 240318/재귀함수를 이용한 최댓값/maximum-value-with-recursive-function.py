def f(n,arr):
    if n == 0:
        return arr[0]
    else:
        return max(arr[n], f(n-1, arr))
    
n=int(input())
arr=list(map(int,input().split()))

print(f(n-1,arr))