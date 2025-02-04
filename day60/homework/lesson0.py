# 1
def to_alternating_case(string):
    return string.swapcase()

# 2
def correct(s):
    return s.replace("5","S").replace("1","I").replace("0","O")

# 3
def bonus_time(s, b):
    return "$" + str(s) + "0" if b else "$" + str(s)

# 4
def is_palindrome(s):
    return s.lower()[::-1] == s.lower()

# 5
def pig_it(text):
    return " ".join(i[1:] + i[0] + "ay" if i.isalpha() else i for i in text.split())

# 6
def move_zeros(lst):
    ll = [i for i in lst if i == 0]
    ls = [i for i in lst if i != 0]
    return ls + ll