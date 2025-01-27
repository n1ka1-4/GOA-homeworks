li = [12,34,45,67,14,40]
print(list(filter(lambda x : x >= 40, li)))
print(list(map(lambda x : x**2, li)))

ll = ["apple","banana","peach","grape"]
print(list(filter(lambda x : x[-1] == "a", ll)))

