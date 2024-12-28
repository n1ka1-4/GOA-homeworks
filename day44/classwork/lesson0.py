#1
def friend(x):
    return [i for i in x if len(i) == 4]
#2
def maskify(cc):
    s = ""
    for _ in cc[0:-4]:
        s += "#"
    return s + cc[-1:-5:-1][::-1]
#3
def add_binary(a,b):
    return bin(a + b).replace("0b","")
#4
def validate_pin(pin):
    if pin.isdigit():
        if 4 == len(pin) or len(pin) == 6:
            return True
        else:
            return False
    return False
#5
def is_triangle(a, b, c):
    return b + c > a and c + a > b and b + a > c

