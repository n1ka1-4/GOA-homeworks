# 1
def plural(n):
    return n != 1

# 2
def problem(a):
    return a * 50 + 6 if a != str(a) else "Error"

# 3
def multi_table(number):
    res = ""
    for i in range(1, 11):
        res += f"{i} * {number} = {i * number}\n"
    return res[:-1]

# 4
def capitalize_word (word : str) -> str:
    return "the first letter was already capitalized" if word[0] == word[0].capitalize() else word[0].capitalize() + word[1:]

# 5
def add_five(num):
    return num + 5