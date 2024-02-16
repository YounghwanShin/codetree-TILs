repet_num=0

while True:
    n = int(input())
    if n%2!=0:
        continue
    else:
        print(n//2)
        repet_num+=1
        if repet_num==3:
            break