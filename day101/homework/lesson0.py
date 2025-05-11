# 1
def burner(c,h,o):
    h2o = co2 = ch4 = 0
    
    while h > 1 and o > 0:
        h2o += 1
        h -= 2
        o -= 1
    
    while c > 0 and o > 1:
        co2 += 1
        c -= 1
        o -= 2
        
    while c > 0 and h > 3:
        ch4 += 1
        c -= 1
        h -= 4
        
    return h2o,co2,ch4

# 2
def stack_height_2d(layers):
    return layers * 1 - ((layers - 1) * 0.134) if layers > 0 else 0

# 3
def height(n):
    h = c = 2000000
    for i in range(n):
        c /= 2.5
        h += c
    return f'{h:.3f}'