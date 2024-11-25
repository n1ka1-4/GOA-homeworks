#1
def basic_op(operator, value1, value2):
    return eval(f"{value1}{operator}{value2}")
#2
def litres(time):
    return int(time * 0.5)
#3
def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return (year // 100)+1
#4
def maps(a):
    s = []
    for i in a:
        s.append(i * 2)
    return s
#5
def digitize(n):
    b = []
    for i in str(n):
        b.insert(0,int(i))
    return b