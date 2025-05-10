# 1
def solve(a,b):
    return "".join(i for i in a if i not in b) + "".join(i for i in b if i not in a)

# 2
def folding(a, b):
    res = 1
    while a != b:
        while a > b:
            res += 1
            a -= b
        while b > a:
            res += 1
            b -= a
    return res

# 3
def valid_card(card):
    return sum([i - 9 if i > 9 else i for i in [int(i) if d % 2 == 0 else int(i) * 2 for d, i in enumerate(reversed(card.replace(" ", "")))]]) % 10 == 0

