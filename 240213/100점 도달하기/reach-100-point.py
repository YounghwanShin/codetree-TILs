n = int(input())

def printf(par):
    print(par, end=" ")

def grade(score):
    if score>=90:
        printf('A')
    elif score>=80:
        printf('B')
    elif score>=70:
        printf('c')
    elif score>=60:
        printf('D')
    else:
        printf('F')

for i in range(n,101):
    grade(i)