# 1
def declare_winner(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:        
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name

# 2
def power_of_two(x):
    return x > 0 and bin(x).count("1") == 1

# 3
def sum_cubes(n):
    return sum(i**3 for i in range(1,n + 1))

# 4
def show_sequence(n):
    return "+".join([str(i) for i in range(n + 1)]) + " = " + str(sum(range(n + 1))) if n > 0 else "0=0" if n == 0 else f"{n}<0"

# 5
def sort_gift_code(code):
    return "".join(sorted(code, key=lambda x: "abcdefghijklmnopqrstuvwxyz".index(x)))

# 6
def even_numbers(arr,n):
    return [i for i in arr if i % 2 == 0][::-1][:n][::-1]

# 7
def vowel_indices(word):
	return [i+1 for i in range(len(word)) if word[i] in "aeiouAEIOUyY"]

# 8
def sort_my_string(s):
    return "".join([s[i] for i in range(len(s)) if i % 2 == 0] + [" "] + [s[i] for i in range(len(s)) if i % 2 == 1])

# 9
def my_languages(results):
    return sorted([i[0] for i in results.items() if int(i[1]) >= 60],key=lambda x: results[x])[::-1]

# 10
def add(n):
    return lambda x: x + n

# 11
def explode(s):
    return "".join([i*int(i) for i in s]) if s.isdigit() and int(s) > 0 else ""

# 12
def mygcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

# 13
def switcheroo(s):
    t = str.maketrans("ab", "ba")
    return s.translate(t)

# 14
def partlist(arr):
    return [(' '.join(arr[:i]), ' '.join(arr[i:])) for i in range(1, len(arr))]

# 15
def sum_triangular_numbers(n):
    return sum([sum(i for i in range(0,i)) for i in range(0,n + 2)][2:])