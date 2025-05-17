# 1
def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name

# 2
def move(position, roll):
    return position + roll * 2

# 3
def enough(cap, on, wait):
    wait = wait - (cap - on)
    if wait < 0:
        return 0
    else:
        return wait
    
# 4
def between(a,b):
    return [i for i in range(a, b + 1)]

# 5
def say_hello(name):
    return "Hello, " + name