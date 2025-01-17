# 1
def update_light(current):
    dict = {
        "green" : "yellow",
        "yellow" : "red",
        "red" : "green"
    }
    return dict[current]

# 2
def twice_as_old(d, s):
    if s == 0:
        return d
    b = 0
    run = True
    while run:
        if d / s < 2:
            s -= 1
            d -= 1
            b += 1
        elif d / s > 2:
            s += 1
            d += 1
            b += 1
        else:
            run = False
    return b

# 3
def is_even(n): 
    return True if n % 2 == 0 and n % 1 == 0 else False

# 4
def uni_total(s):
    b = 0
    for i in s:
        b += ord(i)
        
    return b

# 5
def name_shuffler(str_):
    return " ".join(str_.split()[::-1])