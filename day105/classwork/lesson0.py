# 1
def shift_left(a, b):
    i = len(a) - 1
    j = len(b) - 1
    c = 0
    while i >= 0 and j >= 0 and a[i] == b[j]:
        c += 1
        i -= 1
        j -= 1
    return (len(a) - c) + (len(b) - c)

# 2
def encode(st):
    return "".join(map(str,[ord(i.lower()) - 96 if i.isalpha() else i for i in st]))