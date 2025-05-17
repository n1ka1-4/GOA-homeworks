#1
def remove_char(s):
    return s[1:-1]
#2
def square_sum(numbers):
    result = 0
    for i in numbers:
        result += pow(i,2)
    return result
#3
def find_smallest_int(arr):
    return min(arr)
#4
def string_to_number(s):
    return int(s)
#5
def summation(num):
    x = 0
    for i in range(1,num+1):
        x += i
    return x
#6
def greet():
    return "hello world!"