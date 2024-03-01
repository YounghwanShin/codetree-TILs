n=int(input())
arr_2d = [input() for _ in range(n)]
a = input()

matched = [len(arr) for arr in arr_2d if arr[0] == a]

print(len(matched), f'{sum(matched)/len(matched):.2f}')