N=int(input())
arr=list(map(int,input().split()))

def devide(arr,n):
    for i in range(n):
        if arr[i]%2==0:
            arr[i]=int(arr[i]/2)

devide(arr,N)
print(*arr)