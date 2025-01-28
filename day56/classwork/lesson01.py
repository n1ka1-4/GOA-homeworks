li = [1,2,3,4,5,50,100,200,300,400,50]
print(list(filter(lambda x: x >= 40, li)))
print(list(map(lambda x: x ** 2, li)))

ll = ["apple", "banana", "cherry", "kiwi", "mango"]
print(list(filter(lambda x: x.endswith("a"), ll)))