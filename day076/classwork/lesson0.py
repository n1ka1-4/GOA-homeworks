# 1
def matrix_addition(a, b):
    listn = list(map(sum,list(zip([x for i in a for x in i], [x for i in b for x in i]))))
    res = []
    for i in range(1, len(listn) + 1):
        if i % len(a[0]) == 0:
            res.append(listn[i - len(a[0]) : i])
    return res

# 2
def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    else:
        res1 = ""
        res2 = ""
        for i in range(1, n + 1, 2):
            res1 += " " * list(range(1, n + 1, 2))[::-1].index(i) + "*" * i + "\n"
        
        for i in range(n - 2, 0, -2):
            res2 += " " * (list(range(n - 2, 0, -2)).index(i) + 1) + "*" * i + "\n"
    return res1 + res2