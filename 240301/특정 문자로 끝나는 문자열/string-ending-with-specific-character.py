arr_2d = [input() for _ in range(10)]
a = input()

matched = [arr for arr in arr_2d if arr[-1] == a]

if matched:
    for arr in matched:
        print(arr)
else:
    print('None')