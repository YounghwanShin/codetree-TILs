arr=[input() for _ in range(2)]

new_words_1=''.join(arr)
new_words_2=''.join(arr[::-1])

if new_words_1==new_words_2:
    print('true')
else:
    print('false')