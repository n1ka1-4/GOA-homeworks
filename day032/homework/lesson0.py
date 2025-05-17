#1
def find_average(array):
    return sum(array) / len(array) if array else 0
#2
def smash(words):
    return " ".join(words)
#3
def grow(arr):
    result = 1    
    for i in (arr):
         result *= i
    return result
#4
def hero(bullets, dragons):
    if bullets >= dragons*2:
        return True
    else:
        return False
#5
def better_than_average(class_points, your_points):
    s = 1
    result = 0
    for i in class_points:
        result += i
        s += 1
    if your_points > result / s:
        return True
    else:
        return False
    