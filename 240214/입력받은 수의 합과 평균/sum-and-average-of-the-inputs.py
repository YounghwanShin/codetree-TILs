n=int(input())

arr=[]

for _ in range(n):
    arr.append(int(input()))

sum_val=sum(arr)
ave_val=sum_val/len(arr)
print(sum_val,f"{ave_val:.1f}")