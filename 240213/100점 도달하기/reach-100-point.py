n = int(input())

def prinf(par):
    print(par, end=" ")

def grade(score):
    if score>=90:
        printf('A')
    if score>=80:
        printf('B')
    if score>=70:
        printf('c')
    if score>=60:
        printf('D')
    else:
        printf('F')

for i in range(n,101):
    grade(i)