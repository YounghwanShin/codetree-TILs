n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def is_happy_sequence(sequence):
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            count += 1
            if count >= m:
                return True
        else:
            count = 1
    return False

happy_count = 0

if m==1:
    happy_count = 2*n
else:
    for row in arr:
        if is_happy_sequence(row):
            happy_count += 1

    for col in range(n):
        column = [arr[row][col] for row in range(n)]
        if is_happy_sequence(column):
            happy_count += 1

print(happy_count)