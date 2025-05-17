#1
def longest(a1, a2):
    return "".join(sorted(set(sorted(a1 + a2))))
#2
def open_or_senior(data):
    l = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            l.append("Senior")
        else:
            l.append("Open")
    return l
#3
import math
def find_next_square(sq):
    if math.sqrt(sq) % 1 == 0:
        return (math.sqrt(sq)+1) * (math.sqrt(sq)+1)
    else:
        return -1
#4
def nb_year(p0, percent, aug, p):
    b = 0
    while p0 < p:
            p0 = p0 + p0 * percent//100 + aug
            b += 1
    return b
#5
def reverse_words(s):
    
    word = s.split(" ")  
    
    reversed_words = [wor[::-1] for wor in word]
    return " ".join(reversed_words)
