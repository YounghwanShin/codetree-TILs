A = input()
a = input()

for i in range(len(A) - len(a) + 1):
    if A[i:i+len(a)] == a:
        print(i)
        break
else:
    print(-1)