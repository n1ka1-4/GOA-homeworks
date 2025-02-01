# 1
def shorten_to_date(long_date):
    return long_date.split(',')[0]

# 2
def name_shuffler(str_):
    return " ".join(str_.split()[::-1])

# 3
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# 4
def is_anagram(test, original):
    t = test.lower()
    rgl = original.lower()
    if len(t) != len(rgl):
        return False
    for i in t:
        if t.count(i) != rgl.count(i):
            return False
    else:
        return True
    
# 5
def what_century(year):
    st = str(int(year) // 100 + 1 if int(year) % 100 != 0 else int(year) // 100)
    if st[-1] == "1" and int(st[0]) != 1:
        return st + "st"
    elif st[-1] == "2" and int(st[0]) != 1:
        return st + "nd"
    elif st[-1] == "3" and int(st[0]) != 1:
        return st + "rd"
    else:
        return st + "th"