# 1
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]
   
# 2
def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)

# 3
import math
def get_average(marks):
    return math.floor(sum(marks) / len(marks))

# 4
def reverse_words(s):
    return " ".join(str.split(" ")[::-1])
    
# 5
def check_for_factor(base, factor):
    return base % factor == 0

    