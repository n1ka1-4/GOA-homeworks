# 1
def get_size(w,h,d):
    return [2*(w*h+w*d+h*d),w*h*d]

# 2
def cube_checker(volume, side):
    return False if volume <= 0 or volume <= 0 else volume == side**3

# 3
def pillars(num_pill, dist, width):
    return 0 if num_pill == 1 else (num_pill - 1) * (dist * 100) + (num_pill - 2) * width

# 4
def sum_of_differences(arr):
    return sum([i - sorted(arr)[::-1][b + 1] for b, i in enumerate(sorted(arr)[::-1]) if b != len(arr) - 1])

# 6
def apple(x):
    return "Help yourself to a honeycomb Yorkie for the glovebox." if int(x)**2 < 1000 else "It's hotter than the sun!!"
       
# 7
def generate_range(start, stop, step):
    return list(range(start, stop + 1, step))

# 8
def array(string):
    return None if " ".join(string.split(",")[1:-1]) == "" else " ".join(string.split(",")[1:-1])

# 9
def format_money(amount):
    return f"${amount:.2f}"

# 10
import string
def same_case(a, b): 
    return int(a.isupper() == b.isupper()) if a in string.ascii_letters and b in string.ascii_letters else -1

# 11
def sum_mul(n, m):
    return "INVALID" if n <= 0 or m <= 0 else sum(range(n, m, n))

# 12
def include(arr, item):
    return item in arr

# 13
def derive(c, e): 
    return f"{c*e}x^{e - 1}"

# 14
def nearest_sq(n):
    return round(n**.5)**2

# 15
def get_drink_by_profession(param):
    dict1 = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
    return dict1.get(param.lower(), "Beer")

# 16
def validate_usr(u):
    return all(i in "qazxswedcvfrtgbhynujmkiolp1234567890_" for i in u) if 4 <= len(u) <= 16 else False

# 17
def multiple_of_index(arr):
    return [i for b,i in enumerate(arr) if b != 0 and i % b == 0] if arr[0] != 0 else [0] + [i for b,i in enumerate(arr) if b != 0 and i % b == 0]

# 18
def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_rows - row) * (tot_cols - col + 1)

# 19
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def mod(a, b):
    return a % b

def exponent(a, b):
    return a**b

def subt(a, b):
    return a - b

# 20
def calculate_age(y, c):
    return f"You are {c - y} years old." if c - y > 1 else f"You were born this very year!" if c - y == 0 else f"You will be born in {y - c} years." if y - c > 1 else "You are 1 year old." if c - y == 1 else "You will be born in 1 year."