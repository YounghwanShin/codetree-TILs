arr = list(map(int, input().split()))

multiples_of_3_index = next((i for i, num in enumerate(arr) if num % 3 == 0))

print(arr[multiples_of_3_index - 1])