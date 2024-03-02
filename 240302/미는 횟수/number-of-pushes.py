A = input()
B = input()

for i in range(len(A)):
    if A == B:
        print(i)
        break
    A = A[-1] + A[:-1]
else:
    print(-1)