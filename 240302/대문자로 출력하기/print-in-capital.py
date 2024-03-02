arr=list(input())

for i in arr:
    if 'a'<=i and i<='z':
        print(i.upper(),end='')
    if 'A'<=i and i<='Z':
        print(i,end='')