age_list=[]
while True:
    age=int(input())
    if age>=20 and age<=29:
        age_list.append(age)
    else:
        break

print(f"{sum(age_list)/len(age_list):.2f}")