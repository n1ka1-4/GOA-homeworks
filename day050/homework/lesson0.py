
# 1
username = "world"

try:
    print(name)
except NameError:
    print("name is not defined")

# 2
list1 = [1,2,3,4,"23"]

try:
    print(list1[20000])
except IndexError:
    print("list index out of range")

# 3

try:
    print(int("12.2323houndred"))
except ValueError:
    print("ValueError: int not containes dot (.)")
