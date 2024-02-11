a = int(input())
seasons = {range(3, 6): "Spring", range(6, 9): "Summer", range(9, 12): "Fall", range(1, 3): "Winter", range(12, 13): "Winter"}

for key in seasons:
    if a in key:
        print(seasons[key])
        break