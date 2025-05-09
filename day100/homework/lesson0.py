# 1 
def comes_after(st, l): 
    return "".join([st[i + 1] for i in range(len(st) - 2) if st[i].lower() == l.lower() and st[i + 1].isalpha()])

# 2
def stack_height_2d(layers):
    return layers * 1 - ((layers - 1) * 0.134) if layers > 0 else 0

# 3
def change(st):
    arr = ["0"] * 26
    for i in st:
        if i.isalpha():
            arr[ord(i.lower()) - ord('a')] = "1"
    return "".join(arr)

# 4
def height(n):
    h = c = 2000000
    for i in range(n):
        c /= 2.5
        h += c
    return f"{h:.3f}"

# 5
def chain(ini, f):
    for i in f:
        ini = i(ini)
    return ini

# 6
def bits_battle(numbers):
    odd = []
    even = []
    [odd.append(bin(i)[2:].count("1")) if i % 2 == 1 else even.append(bin(i)[2:].count("0")) for i in [i for i in numbers if i != 0]]
    if sum(odd) > sum(even):
        return "odds win"
    elif sum(even) > sum(odd):
        return "evens win"   
    else:
        return "tie"
    
# 7
def largest_sum(s):
    return max([sum(map(int,[x for x in i])) for i in [i for i in s.split("0")] if i != ""]) if s != "0" else 0

# 8
def decode(message):
    return message.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"))

# 9
def invert_hash(dic):
    return {y: x for x, y in dic.items()}

# 10
def create_box(m, n):
    return [[min([j+1, i+1, m-j, n-i]) for j in range(m)] for i in range(n)]