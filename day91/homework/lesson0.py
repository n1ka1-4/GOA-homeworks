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