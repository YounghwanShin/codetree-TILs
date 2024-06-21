n=int(input())
N=list(map(int, input().split()))
N.sort()

results=[]
i=0
p=len(N)

while i<n:
    results.append((N[i],N[p-i-1],N[i]+N[p-1-i]))
    i+=1

max_val = 0
for k in range(len(results)):
    if results[k][2]>max_val:
        max_val=results[k][2]

print(max_val)