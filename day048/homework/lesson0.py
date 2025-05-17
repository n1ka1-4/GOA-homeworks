# 1
def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"
# 2
import math
def cockroach_speed(s):
    return math.floor(s * 27.7777778)
# 3
def switch_it_up(number):
    dict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"}
    
    return dict[number]
# 4
def square(n):
    return n**2
# 5
def remove_every_other(my_list):
    return my_list[::2]