def check_adult(age, gender):
    return int(age) >= 19 and gender == 'M'

a = input().split()
b = input().split()

print(1 if check_adult(*a) or check_adult(*b) else 0)