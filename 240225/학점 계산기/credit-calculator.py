n = int(input())
arr = list(map(float, input().split()))

aver = sum(arr) / n
print(f'{aver:.1f}')

messages = [(4.0, 'Perfect'), (3.0, 'Good'), (0, 'Poor')]

for limit, message in messages:
    if aver >= limit:
        print(message)
        break