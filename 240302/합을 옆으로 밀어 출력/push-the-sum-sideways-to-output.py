n=int(input())

val=0

for _ in range(n):
    val+=int(input())

string=str(val)
print(string[1:]+string[0])