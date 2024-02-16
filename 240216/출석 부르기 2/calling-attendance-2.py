attendance_book = {1:'John', 2:'Tom', 3:'Paul', 4:'Sam'}

while True:
    n=int(input())
    if n in attendance_book:
        print(attendance_book[n])
    else:
        print('Vacancy')
        break