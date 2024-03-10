A=input()
B=input()

def f():
    if B in A:
        return A.index(B)
    else:
        return -1

print(f())