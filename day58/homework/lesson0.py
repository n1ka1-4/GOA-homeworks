# 1
def who_is_paying(name):
    return [name,name[:2]] if name[:2] != name else [name]

# 2
def odd_count(n):
    return n // 2

# 3
import string
def is_uppercase(inp):
    return all([i.isupper() for i in inp if i in string.ascii_letters])

# 4
def grader(s):
    if s > 1 or s < 0.6:
        return "F"
    elif s >= 0.9:
        return "A"
    elif s >= 0.8:
        return "B"
    elif s >= 0.7:
        return "C"
    elif s >= 0.6:
        return "D"
    
# 5
def if_chuck_says_so():
    return 0 and 1
