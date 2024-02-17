arr=[]
for _ in range(5):
    arr.append(int(input()))

all_num = all(number % 3 == 0 for number in arr)

if all_num ==True:
    print(1)
else:
    print(0)