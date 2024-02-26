arr = list(map(int, input().split()))

i=0

while i<=len(arr)-1:
    if arr[i]%2==0 and arr[i]!=0:
        print(arr[i]//2, end=' ')
    elif arr[i]!=0:
        print(arr[i]+3, end=" ")
    i+=1