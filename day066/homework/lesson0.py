# 1
def count_red_beads(n):
    return int(n * 2 - 2)

# 2
def generate_shape(n):
    return str(n * f"{n * '+'}\n")[:-1]

# 3
def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"

# 4
def adjacent_element_product(array):
    max_num = float('-inf')
    for i in range(len(array) - 1):
        product = array[i] * array[i + 1]
        if product > max_num:
            max_num = product
    return max_num

# 5
def filter_string(st):
    return int("".join([i for i in st if i.isdigit()]))