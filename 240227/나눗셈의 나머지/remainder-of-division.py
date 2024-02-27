a,b=map(int, input().split())

arr=[0]*b

while a>1:
    arr[a%b]+=1
    a=a//b

new_arr=[i**2 for i in arr]

print(sum(new_arr))