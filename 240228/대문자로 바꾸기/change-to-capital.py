arr_2=[list(input().split()) for _ in range(5)]

for arr in arr_2:
    print(*[chr(ord(i)-32) for i in arr])