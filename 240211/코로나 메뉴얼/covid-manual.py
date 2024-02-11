def put(input_string):
    cold, temp = input_string.split()
    return cold, int(temp)

A_count = 0

def decision(cold, temp):
    global A_count
    if cold == 'Y' and temp >= 37:
        A_count += 1

A, a = put(input())
B, b = put(input())
C, c = put(input())

decision(A, a)
decision(B, b)
decision(C, c)

if A_count >= 2:
    print("E")
else:
    print('N')