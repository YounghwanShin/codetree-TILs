def count_leap_years(year):
    leap_years = 0
    for i in range(1, year+1):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            leap_years += 1
    return leap_years

year = int(input())
print(count_leap_years(year))