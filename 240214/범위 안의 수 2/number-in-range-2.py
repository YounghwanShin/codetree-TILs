val=[]

for _ in range(10):
    n=int(input())
    if n>=0 and n<=200:
        val.append(n)

sum_val=sum(val)
len_val=len(val)
ave_val=sum_val/len_val
print(sum_val,f"{ave_val:.1f}")