from decimal import Decimal, getcontext

# 소수점 이하 21자리까지 정확도를 보장하도록 설정
getcontext().prec = 21

# 입력 받기
a, b = map(Decimal, input().split())

# 나눗셈 수행
result = a / b

# 결과 출력 (소수점 이하 20자리까지)
print("{:.20f}".format(result))