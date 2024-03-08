a,o,c=input().split()
a,c=int(a),int(c)

def dot(a,c):
    return a*c

def hap(a,c):
    return a+c

def cha(a,c):
    return a-c

def na(a,c):
    return a//c

if o=='+':
    print(f'{a} {o} {c} = {hap(a,c)}')
elif o=='-':
    print(f'{a} {o} {c} = {cha(a,c)}')
elif o=='*':
    print(f'{a} {o} {c} = {dot(a,c)}')
elif o=='/':
    print(f'{a} {o} {c} = {dot(a,c)}')
else:
    print('False')