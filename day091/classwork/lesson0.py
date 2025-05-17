# kyu 8

# 1
def to_binary(n):
    return int(bin(n)[2:])

# 2
def hello(name="World"):
    if not name:
        name = "World"
    return f"Hello, {name.capitalize()}!"

# 3
import math
def square_or_square_root(arr):
    for i in range(len(arr)):
        if math.sqrt(arr[i]) % 1 == 0:
            arr[i] = math.sqrt(arr[i])
        else:
            arr[i] = arr[i]**2
    return arr

# kyu 7

# 1
def row_sum_odd_numbers(n):
    return n**3

# 2
def triangular(n):
    return 0 if n < 1 else sum([i for i in range(1, n + 1)])

# 3
def min_value(digits):
    return int("".join(map(str,sorted(set(digits)))))

# 4
def sum_of_minimums(numbers):
    return sum(min(i) for i in numbers)