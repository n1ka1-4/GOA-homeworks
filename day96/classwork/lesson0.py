# kyu 8

# 1
def chromosome_check(chromosome):
    return 'Congratulations! You\'re going to have a son.' if chromosome[-1] == "Y" else 'Congratulations! You\'re going to have a daughter.'

# 2
def bin_to_decimal(inp):
    return int(inp,2)

# 3
def main(verb, noun):
    return verb + noun

# 4
def mango(quantity, price):
    return sum(price for i in range(1,quantity+1) if i % 3 != 0)

# 5
def duty_free(price, discount, holiday_cost):
    return holiday_cost // (price * (discount / 100))

# 6
def remove(s):
    return "" if s == "" else s[:-1] if s[-1] == "!" else s

# 7
def hex_to_dec(s):
    return int(s,16)

# 8
def say_hello(name, city, state):
    return f'Hello, {" ".join(name)}! Welcome to {city}, {state}!'

# 9
def take(arr,n):
    res = 0
    for i in range(len(arr)):
        if n == res:
            return arr[:i]
        else: res += 1
    else:
        return arr
    
# 10
def reverse(st):
    return " ".join(st.split()[::-1])

# 11
def whatday(num):
    match num:
        case 1: return "Sunday"
        case 2: return "Monday"
        case 3: return "Tuesday"
        case 4: return "Wednesday"
        case 5: return "Thursday"
        case 6: return "Friday"
        case 7: return "Saturday"
        case _: return 'Wrong, please enter a number between 1 and 7'

# 12
def print_array(arr):
    return ",".join(map(str,arr))

# 13
def remainder(*a):
    return None if min(a) == 0 else max(a) % min(a)

# 14
def correct_tail(body, tail):
     return body[-1] == tail

# 15
def string_clean(s):
    return "".join(i for i in s if i not in "1234567890")
