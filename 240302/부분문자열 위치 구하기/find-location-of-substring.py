A=input()
a=input()

for i in range(len(a),len(A)):
    val=True
    for k in range(len(a),0,-1):
        if A[i-k]!=a[len(a)-k]:
            val=False
    if val==True:
        print(i-len(a))
        break