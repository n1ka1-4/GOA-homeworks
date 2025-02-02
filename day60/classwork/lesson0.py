# 1
def create_phone_number(n):
    n = "".join([str(i) for i in n])
    return f"({n[:3]}) {n[3:6]}-{n[6:]}"
        
# 2
def likes(names):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"
    
# 3
def find_it(seq):
    return max([i for i in seq if seq.count(i) % 2 == 1])