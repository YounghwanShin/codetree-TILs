A=input()

cnt=0

for char in A:
    if char.isdigit():
        cnt+=int(char)

print(cnt)