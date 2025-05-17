def manual_find(x,day):
    b = 0
    for i in x:
        if i == day:
            return b
        else:
            b += 1
    return -1


import string
def manual_swapcase(x):
    str1 = ""
    list1 = []
    list2 = []
    for i in string.ascii_lowercase:
        list1.append(i)
    for i in string.ascii_uppercase:
        list2.append(i)
    for b in x:
        if b in list1:
            str1 += list2[list1.index(b)]
        else:
            str1 += list1[list2.index(b)]
    return str1


