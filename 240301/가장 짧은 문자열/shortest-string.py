inputs = [input() for _ in range(3)]
lengths = [len(i) for i in inputs]

print(max(lengths) - min(lengths))