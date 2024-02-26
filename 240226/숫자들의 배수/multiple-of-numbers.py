n=int(input())

arr=[n]
val=0

for i,num in enumerate(arr):
    arr.append(arr[i]+n)
    print(num, end=' ')
    if arr[i]%5==0:
        val+=1
        if val==2:
            break