#1
def high_and_low(numbers):
    lis = numbers.split()
    lis = [int(i) for i in lis]
    return f"{max(lis)} {min(lis)}"
#2
def filter_list(l):
    l = [i for i in l if i != str(i)]
    return l
#3
def descending_order(num):
    l = []
    n = [l.append(int(i)) for i in str(num)]
    l = [int(i) for i in l]
    st = ""
    for i in range(len(l)):
        st += str(max(l))
        l.remove(max(l))
    return int(st)
#4
import math
def is_square(n):    
    return False if n < 0 else math.sqrt(n) % 1 == 0
#5
def get_middle(s):
    if len(s) % 2 == 0:
        y = len(s) // 2 -1
        x = len(s) // 2 + 1
        return s[y : x]
    else:
        y = len(s) // 2
        x = len(s) // 2 + 1
        return s[y : x]