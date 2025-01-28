# 1
import string
def is_uppercase(inp):
    return all([i.isupper() for i in inp if i in string.ascii_letters])

# 2
def monkey_count(n):
    return list(range(1,n+1))

# 3
def powers_of_two(n):
    return [2**i for i in range(n+1)]

# 4
def human_years_cat_years_dog_years(h):
    ll = [h]
    res = 0
    for i in range(h):
        if i == 0:
            res += 15
        elif i == 1:
            res += 9
        else:
            res += 4
    ll.append(res)
    res = 0
    for i in range(h):
        if i == 0:
            res += 15
        elif i == 1:
            res += 9
        else:
            res += 5
    ll.append(res)
    return ll

# 5
def first_non_consecutive(arr):
    j = 0
    i = 1
    for h in arr: 
        try:
            if arr[j] + 1 != arr[i]:
                return arr[i]
        except IndexError:
            return None
        j += 1
        i += 1