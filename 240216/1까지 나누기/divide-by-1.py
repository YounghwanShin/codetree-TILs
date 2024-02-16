n= int(input())

repetition=0

for i in range(1, n+1):
    repetition+=1
    n=n/i
    if n<=1:
        break

print(repetition)