# mutable - list, dict 
# immutable - str, tuple, set (set - add და remove შეგიძლია)
# lambda - anonymous functions
# map ში ვატარებთ და ცვლის და filter თუ ფელს აჩვენებს არ თვლის
# str + str = concatenation

print(list(map(lambda i : i**2,[1,2,3,4,5])))
print(list(map(lambda i : i * 33.8,[0, 20, 30, 40])))
print(list(map(lambda i : i.capitalize(),["hello", "world", "python"])))



print(list(filter(lambda i : i % 2 == 0,[1, 2, 3, 4, 5, 6, 7, 8])))
print(list(filter(lambda i : len(i) >= 4,["cat", "house", "tree", "car"])))
print(list(filter(lambda i : i % 3 == 0,[3, 9, 15, 22, 27, 30])))