n=int(input())

arr=list(map(int, input().split()))

if n==1:
    print(arr[0])
else:
    for i in range(n):
        max_index=i
        for j in range(i+1,n):
            if arr[max_index]<arr[j]:
                max_index=j
        arr[i],arr[max_index]=arr[max_index],arr[i]

    if arr[0]!=arr[1]:
        print(arr[0])
    else:
        for k in range(1,n):
            if arr[k]!=arr[k+1] and arr[k-1]!=arr[k]:
                print(arr[k])
                break
        else:
            print(-1)