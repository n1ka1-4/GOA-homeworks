# 1
def in_asc_order(arr):
    return sorted(arr) == arr

# 2
def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    
    max_a1, min_a1 = len(sorted(a1,key=len)[0]), len(sorted(a1,key=len)[-1])
    max_a2, min_a2 = len(sorted(a2,key=len)[0]), len(sorted(a2,key=len)[-1])
    
    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))

# 3
def flatten_and_sort(array):
    if not array:
        return []
    else:
        lis = []
        for i in array:
            lis += i
    return sorted(lis)

# 4
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# 5
def fizzbuzz(n):
    ll = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            ll.append("FizzBuzz")
        elif i % 5 == 0:
            ll.append("Buzz")
        elif i % 3 == 0:
            ll.append("Fizz")
        else:
            ll.append(i)
    return ll

# 6
def row_weights(a):
    tu = []
    tu.append(sum([a[i] for i in range(0, len(a), 2)]))
        
    tu.append(sum([a[i] for i in range(1, len(a), 2)]))
    
    return tuple(tu)

# 7
def greet(name): 
    return f"Hello {name.lower().capitalize()}!"

# 8
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending' 
    elif arr == sorted(arr)[::-1]:
        return 'yes, descending'
    else:
        return 'no'
    
# 9
def remove_duplicate_words(s):
    return " ".join(sorted(list(set(s.split()[::-1])), key=lambda x: s.index(x)))