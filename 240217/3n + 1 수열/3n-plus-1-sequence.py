n = int(input())
repet=0

while True:
    if n%2==0:
        n=n/2
    elif n!=1:
        n=n*3+1
    repet+=1
    if n==1:
        break

print(repet)