n=int(input())
arr=list(map(float, input().split()))

aver=sum(arr)/n

print(f'{aver:.1f}')

if aver>=4.0:
    print('Perfect')
elif aver>=3.0:
    print('Good')
else:
    print('Poor')