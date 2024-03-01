arr_2d=["apple", "banana", "grape", "blueberry", "orange"]
a=input()

cnt=0

for arr in arr_2d:
    if arr[2]==a or arr[3]==a:
        cnt+=1
        print(arr)

print(cnt)