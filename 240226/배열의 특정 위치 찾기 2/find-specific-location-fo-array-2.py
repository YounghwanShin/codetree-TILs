arr=list(map(int, input().split()))

cnt_1, cnt_2=0,0

for i,num in enumerate(arr):
    if (i+1)%2==0:
        cnt_1+=num
    else:
        cnt_2+=num

result = abs(cnt_1 - cnt_2)

print(result)