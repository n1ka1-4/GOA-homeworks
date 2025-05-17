# 1
def count_repeats(txt):
    return sum(1 for i in range(len(txt) - 1) if txt[i] == txt[i + 1])

# 2
def tower_builder(n):
    return [("*" * i).center(int(n * 1.99)) for i in range(1, n * 2, 2)]

# 3
def sortme(words):
    return sorted(words, key=lambda x: x.lower())