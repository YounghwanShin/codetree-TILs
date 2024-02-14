a,b=map(int, input().split())

val=[]

for i in range(a,b+1):
    if i%5==0 or i%7==0:
        val.append(i)

sum_val=sum(val)
len_val=len(val)
average_val=sum(val)/len(val)
print(sum_val,f"{average_val:.1f}")