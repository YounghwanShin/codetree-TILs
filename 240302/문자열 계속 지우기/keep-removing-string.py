A=input()
B=input()
arr_A,arr_B=list(A),list(B)

while True:
    if B in A:
        a=A.find(B)
        arr_A=arr_A[0:a]+arr_A[a+len(B):]
        A=''.join(arr_A)
    else:
        break

print(A)