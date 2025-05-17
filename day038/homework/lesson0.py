#1
def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return (l + w) * 2
#2
def other_angle(a,b):
    return 180 - a - b
#3
def set_alarm(employed, vacation):
    if employed == vacation:
        return False
    elif employed == False:
        return False
    else:
        return True
#4
def sum_mix(arr):
    return sum([int(i) for i in arr])
#5
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)