n=int(input())

sum=0

for i in range(1,101):
    if sum+i>=n:
        break
    else:
        sum+=i
print(sum)