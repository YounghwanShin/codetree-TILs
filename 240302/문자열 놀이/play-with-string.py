s,q=input().split()
s,q=list(s),int(q)

def answer(num,a,b):
    global s
    if num==1:
        a,b=int(a)-1,int(b)-1
        val=s[a]
        s[a]=s[b]
        s[b]=val
    elif num==2:
        val=a
        for i in range(len(s)):
            if s[i]==val:
                s[i]=b

    print(''.join(s))

for _ in range(q):
    num,a,b=input().split()
    num=int(num)
    answer(num,a,b)