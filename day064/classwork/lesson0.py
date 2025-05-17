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

# 6
def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [i for i in birds if i not in geese]

# 7
def divisible_by(numbers, divisor):
    return [i for i in numbers if i % divisor == 0]

# 8
def name_shuffler(str_):
    return " ".join(str_.split()[::-1])

# 9
def pipe_fix(nums):
    return [i for i in range(min(nums), max(nums) + 1)]

# 10
def sale_hotdogs(n):
    if n < 5:
         return n * 100
    elif 5 and n < 10:
        return n * 95
    else:
        return n * 90