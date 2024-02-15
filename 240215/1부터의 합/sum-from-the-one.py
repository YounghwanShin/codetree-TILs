n=int(input())

sum=0

for i in range(1,n+1):
    if sum+i<n:
        sum+=i
    else:
        break
print(sum)