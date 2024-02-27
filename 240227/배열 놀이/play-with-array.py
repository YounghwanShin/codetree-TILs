n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    query_type = query[0]
    
    if query_type == 1:
        a = query[1]
        print(arr[a-1])
    elif query_type == 2:
        a = query[1]
        try:
            print(arr.index(a) + 1)
        except ValueError:
            print(0)
    else:
        a, b = query[1], query[2]
        for i in range(a-1, b):
            print(arr[i], end=' ')
        print()