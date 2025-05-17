print(list(map(lambda b : b * 2, [2,4,6,8,10])))
print(list(map(lambda b : "hello " + b, ["Alice", "Bob", "Charlie"])))
print(list(map(lambda b : len(b), ["apple", "banana", "kiwi"])))

print(list(filter(lambda b : b >= 0, [-5, 3, -2, 7, 0, 10])))
print(list(filter(lambda b : b[0] == "p", ["pear", "apple", "peach", "grape"])))
print(list(filter(lambda b : b > 50, [10, 55, 42, 78, 65, 20])))
