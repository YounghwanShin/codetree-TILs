Y, M, D = map(int, input().split())

def is_leap_year(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def get_season(m):
    if m in [3, 4, 5]:
        return 'Spring'
    elif m in [6, 7, 8]:
        return 'Summer'
    elif m in [9, 10, 11]:
        return 'Fall'
    else: # m in [12, 1, 2]
        return 'Winter'

def main(y, m, d):
    if m in [1, 3, 5, 7, 8, 10, 12] and d <= 31:
        print(get_season(m))
    elif m in [4, 6, 9, 11] and d <= 30:
        print(get_season(m))
    elif m == 2 and ((is_leap_year(y) and d <= 29) or (not is_leap_year(y) and d <= 28)):
        print(get_season(m))
    else:
        print(-1)

main(Y, M, D)