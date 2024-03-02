s = input()

result = ''

for char in s:
    if char.isalpha() or char.isdigit():
        result += char.lower()

print(result)