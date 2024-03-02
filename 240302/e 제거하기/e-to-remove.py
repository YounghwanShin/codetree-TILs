A = input()
A_list = list(A)

i = A_list.index('e')
A_list.pop(i)

A = ''.join(A_list)

print(A)