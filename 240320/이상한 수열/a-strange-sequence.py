#점화식: T(n)=T(n/3보다 작은 정수 중 max)+T(n-1)

def T(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    
    return T(int(n/3))+T(n-1)   #//으로도 바닥함수 구현 가능.

n=int(input())
print(T(n))