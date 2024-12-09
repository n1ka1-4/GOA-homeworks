#1
def rental_car_cost(d):
    if d * 40 >= 280:
        return d * 40 - 50
    elif d * 40 >= 120:
        return d * 40 - 20
    else:
        return d * 40
#2
def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4
#3
def remove_exclamation_marks(s):
    name = ""
    for i in s:
        if i != "!":
            name += i
        else:
            name += ""
    return name
#4
def points(games):
    res = 0
    for i in games:
        if i[0] > i[-1]:
            res += 3
        elif i[0] < i[-1]:
            res += 0
        else:
            res += 1
    return res
#5
def get_volume_of_cuboid(length, width, height):
    return length * width * height