# 1
def find_children(e):
    letter = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    return "".join(sorted(e, key=lambda x: letter.index(x)))

# 2
def string_transformer(s):
    return " ".join(s.split(" ")[::-1]).swapcase()

# 3
def hamming(a,b):
    rs = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            rs += 1
    return rs

