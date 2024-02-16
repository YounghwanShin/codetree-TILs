n= int(input())

repetition=0

for i in range(1, n+1):
    n=n//i
    if n<=1:
        break
    repetition+=1

print(repetition)