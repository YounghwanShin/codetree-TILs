def long_division(numerator, denominator, decimal_places):
    quotient = numerator // denominator
    remainder = numerator % denominator
    result = str(quotient) + "."

    for _ in range(decimal_places):
        remainder *= 10
        quotient = remainder // denominator
        remainder %= denominator
        result += str(quotient)

    return result

a, b = map(int, input().split())
print(long_division(a, b, 20))