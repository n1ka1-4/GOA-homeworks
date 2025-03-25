# 1
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
    

# 2
def dig_pow(n, p):
    res = 0
    for i in str(n):
        res += int(i)**p
        p += 1
    
    if res // n * n != res:
        return -1
    else:
        return res // n
    
# 3
def matrix_div(r,m,n):
    return [[r[i][j][j]//m[j][j] for j in range(len(m))] for i in range(len(m))] if n else [[r[i][j][i]//m[i][i] for j in range(len(m))] for i in range(len(m))]

# 4
def draw_stairs(n):
    return "".join([" " * i + "I\n" for i in range(n)])[:-1]
    
# 5
def usdcny(usd):
    return f'{usd * 6.75:.2f} Chinese Yuan'

