a, b = map(int, input().split())
reward = 0

if a >= 90:
    reward = 50000 if b >= 90 else 0
    if b >= 95:
        reward = 100000

print(reward)