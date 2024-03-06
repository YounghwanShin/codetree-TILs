N=int(input())

def _sum(N):
    key=0
    for i in range(1,N+1):
        key+=i
    return key/10

print(int(_sum(N)))