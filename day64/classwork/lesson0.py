# 1
def find_multiples(integer, limit):
    return list(range(integer, limit+1,integer))

# 2
a = "code"
b = "wa.rs"
name = a + b

# 3
def create_array(n):
    res=[]
    i=0
    while i < n: 
        i += 1
        res.append(i)
    return res

# 4
def xor(a,b):
    return False if a == b else True

# 5
def get_real_floor(n):
    return n - 2 if n >= 13 else 0 if n == 0 else n - 1 if n > 0 else n