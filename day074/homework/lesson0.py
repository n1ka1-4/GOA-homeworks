# 1
import math
def get_participants(n):
    return math.ceil((1 + math.sqrt(8 * n + 1)) / 2) if n > 0 else 0

# 2
def delete_nth(o,m):
    ll = o[::-1]
    for _ in range(100):
        for i in ll:
            while ll.count(i) > m:
                ll.remove(i)
    return ll[::-1]

# 3
def missing_values(seq): 
    return sorted(seq, key=lambda x: seq.count(x))[0] ** 2 * sorted(seq, key=lambda x: seq.count(x))[1]

# 4
def compose(s1, s2):
    res = ""
    s11, s12 = s1.split("\n"), s2.split("\n")[::-1]
    for i in range(len(s11)):
        res += s11[i][:i+1] + s12[i][:len(s11) - i] + "\n"
    return res[:-1]


