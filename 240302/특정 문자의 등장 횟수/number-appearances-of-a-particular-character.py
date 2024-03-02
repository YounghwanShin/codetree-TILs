A=input()

cnt_1,cnt_2=0,0

for i in range(1,len(A)):
    if A[i-1]=='e':
        if A[i]=='e':
            cnt_1+=1
        elif A[i]=='b':
            cnt_2+=1

print(cnt_1,cnt_2)