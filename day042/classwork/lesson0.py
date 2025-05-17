#1
def is_isogram(string):
    return len(set(string.lower())) == len(string)
#2
def xo(s):
    l = [i for i in s.lower() if i == "x" or i == "o"]
    return l.count("o") == l.count("x")
#3
def to_jaden_case(string):
    s = string.split()
    st = ""
    for i in s:
        st += f"{i.capitalize()} "
    st = st[0:-1]
    return st
#4
def find_short(s):
    return min([len(i) for i in s.split()])
