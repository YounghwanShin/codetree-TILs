arr=list(map(int, input().split()))

result_1=0
result_2=0

sum_1=0
sum_2=0

n=0

for i,num in enumerate(arr):
    if (i+1)%3==0:
        sum_2+=num
        n+=1
    if (i+1)%2==0:
        sum_1+=num

print(sum_1,f'{sum_2/n:.1f}')