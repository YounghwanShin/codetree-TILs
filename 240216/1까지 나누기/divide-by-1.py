n= int(input())

repetition=0

for i in range(1, n+1):
    n=n//i
    repetition+=1
    if n<=1:
        break

print(repetition)