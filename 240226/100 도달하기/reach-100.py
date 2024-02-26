n=int(input())

arr=[1,n]
i=0

for num in arr:
    print(num, end=' ')
    arr.append(arr[i]+arr[i+1])
    i+=1
    if num>=100:
        break