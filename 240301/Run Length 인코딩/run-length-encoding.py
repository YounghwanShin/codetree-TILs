from itertools import groupby

A = input()
arr = [(k, len(list(g))) for k, g in groupby(A)]

words = ''.join([k + str(num) for k, num in arr])

print(len(words))
print(words)