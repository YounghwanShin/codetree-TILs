Yoon_Year=0

year=int(input())

for i in range(1, year+1):
    if i%4==0:
        if i%100==0 and i%400!=0:
            continue
        else:
            Yoon_Year+=1
    else:
        continue

print(Yoon_Year)