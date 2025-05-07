# 1
def get_ascii(ch : str) -> int:
    return ord(ch)

# 2
def calculator(x, y, op):
    if op == "+" and type(x) == int and type(y) == int: return x + y
    elif op == "-" and type(x) == int and type(y) == int: return x - y
    elif op == "*" and type(x) == int and type(y) == int: return x * y
    elif op == "/" and type(x) == int and type(y) == int: return x / y 
    else: return "unknown value"

# 3
def was_package_received_yesterday(tz_from, tz_to, start, duration):
    return True if start - (tz_from - tz_to - duration) < 0 else False

# 4
def quote(fighter):
    return "I'd like to take this chance to apologize.. To absolutely NOBODY!" if fighter.lower() == "conor mcgregor" else "I am not impressed by your performance."

# 5
def alias_gen(f_name, l_name):
    return FIRST_NAME[f"{f_name[0].upper()}"] + " " + SURNAME[f"{l_name[0].upper()}"] if f_name[0].isalpha() and l_name[0].isalpha() else 'Your name must start with a letter from A - Z.'

# 6
def is_digit(n):
    return len(n) == 1 and n.isdigit()


# 6 kyu

# 1
def spin_words(se):
    return " ".join([i if len(i) < 5 else i[::-1] for i in se.split()])

# 2
def encode(st):
    return st.translate(str.maketrans("aeiou","12345"))
    
def decode(st):
    return st.translate(str.maketrans("12345","aeiou"))
