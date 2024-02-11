AM, AE = map(int, input().split())
BM, BE = map(int, input().split())

if AM != BM:
    print("A" if AM > BM else "B")
else:
    print("A" if AE > BE else "B")