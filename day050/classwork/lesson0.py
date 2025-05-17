# IndexError - გვაქ ლისტი რომელიც ლიგრძეა 3 და ჩვენ ვიჩახებთ 3 ან მეტს
# NameError - როცა ვიჩახებთ სახელს რომელიც არ არსებობს
# ValueError - როცა მაგ: სტრინგს ვაქცევ int ან float-ად
# TypeError - როცა მაგ: int ვუმატებთ str
# SyntaxError - როცა მაგ: if გამოვიყენე და ბოლოში ორწერტილი არ დაუწერე
# ZeroDivisionError - როცა რამეს ვყობთ ნულზე


# 1
name = "hello"

try:
    print(username)
except NameError:
    print("username is not defined")

# 2
list1 = [1,2,3,4]

try:
    print(list1[4])
except IndexError:
    print("list index out of range")

# 3

try:
    print(int("12.23"))
except ValueError:
    print("ValueError: int not containes dot (.)")


# try/except - ვიყენებთ დიბაგისთვის მაგ ჩალიან გამოსადეგარია უსერთან მშაობისას