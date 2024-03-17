def f(n,arr):
    if n == 0:
        return arr[0]
    else:
        prev_max = f(n-1, arr)
        if arr[n] > prev_max:
            return arr[n] 
        else:
            return prev_max
    
n=int(input())
arr=list(map(int,input().split()))

print(f(n-1,arr))