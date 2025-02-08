# 1
def final_grade(e, p):
    if e > 90 or p > 10:
        return 100
    elif e > 75 and p >= 5:
        return 90
    elif e > 50 and p >= 2:
        return 75
    else:
        return 0
    
# 2
def expression_matter(a, b, c):
    ll = [a + b + c, a * b * c, a + b * c, a * b + c, (a + b) * c, a * (b + c)]
    return max(ll)

# 3
def sum_str(n,n1):
    if n.isdigit() and n1.isdigit():
        return str(int(n) + int(n1))
    else:
        if n.isdigit():
            return n
        elif n1.isdigit():
            return n1
        else:
            return "0"
        
# 4
def how_much_i_love_you(n):
    n = n % 6
    match n:
        case 1:
            return "I love you"
        case 2:
            return "a little"
        case 3:
            return "a lot"
        case 4:
            return "passionately"
        case 5:
            return "madly"
        case 0:
            return "not at all"

# 5
def reverse_list(l):
    return l[::-1]
