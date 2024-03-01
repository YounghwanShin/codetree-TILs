A=input()

new_A=''

for i in A[1:len(A):2]:
    new_A+=i

print(new_A[::-1])