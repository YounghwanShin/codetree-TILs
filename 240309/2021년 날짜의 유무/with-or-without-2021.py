M,D=map(int, input().split())

def d_31(d):
    if d<=31:
        return True
    else:
        return False
    
def d_30(d):
    if d<=30:
        return True
    else:
        return False

def pprint(val):
    if val:
        print('Yes')
    else:
        print('No')


if M in [1,3,5,7,8,10,12]:
    pprint(d_31(D))
elif M in [4,6,9,11]:
    pprint(d_30(D))
elif M==2:
    if D<=28:
        print('Yes')
    else:
        print('No')
else:
    print('No')