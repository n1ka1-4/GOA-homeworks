#1
def lovefunc( flower1, flower2 ):
    if flower1 % 2 != flower2 % 2:
        return True
    else:
        return False
#2
def sum_array(a):
    b = 0
    if a == False:
        return 0
    else:
        for i in a:
            b += i
        return b
#3
def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return n * m
#4
def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        y = 3600 * h
        x = 60 * m 
        return (y + x + s) * 1000
    else:
        return None
#5
def make_upper_case(s):
    return s.upper()