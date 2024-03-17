def f(n,arr):
    if n==0:
        return arr[n]
    
    if arr[n]<f(n-1,arr):
        return arr[n-1]
    else:
        return arr[n]
    
n=int(input())
arr=list(map(int,input().split()))

print(f(n-1,arr))