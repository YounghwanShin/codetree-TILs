a = int(input())
if a%2!=0 and a%3==0:
    a=(a+3)/3
elif a%2!=0:
    a+=3
print(int(a))