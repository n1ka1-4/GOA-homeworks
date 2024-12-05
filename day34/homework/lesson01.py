#1
def fake_bin(x):
    return x.replace("1","0").replace("5","1").replace("4","0").replace("3","0").replace("2","0").replace("9","1").replace("8","1").replace("7","1").replace("6","1").replace("5","1")
#2
def string_to_array(s):
    if s == "" or s == '':
        return [s]
    else:
        return s.split()
#3
def check(seq, elem):
    return elem in seq
#4
def reverse_seq(n):
    b = n-1
    list1 = []
    for i in range(1,n+1):
        list1.append(i+b)
        b -= 2
    return list1
#5
def count_by(x, n):
    return list(range(x,n * x+1,x))