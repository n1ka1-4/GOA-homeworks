#1
def rps(p1, p2):
    if p1[0] == "r" and p2[0] == "s":
        return "Player 1 won!"
    elif p1[0] == "r" and p2[0] == "p":
        return "Player 2 won!"
    elif p1[0] == "s" and p2[0] == "r":
        return "Player 2 won!"
    elif p1[0] == "s" and p2[0] == "p":
        return "Player 1 won!"
    elif p1[0] == "p" and p2[0] == "r":
        return "Player 1 won!"
    elif p1[0] == "p" and p2[0] == "s":
        return "Player 2 won!"
    else:
        return "Draw!"
#2
def is_divisible(n,x,y):
    return True if n % x == 0 and n % y == 0 else False
#3
def count_sheep(n):
    res = ""
    for i in range(1,n+1):
        res += f"{i} sheep..."
    return res
#4
def get_grade(s1, s2, s3):
    if 90 <= ((s2 + s1 + s3) // 3) <= 100:
        return "A"
    elif 80 <= ((s2 + s1 + s3) // 3) < 90:
        return "B"
    elif 70 <= ((s2 + s1 + s3) // 3) < 80:
        return "C"
    elif 60 <= ((s2 + s1 + s3) // 3) < 70:
        return "D"
    elif 0 <= ((s2 + s1 + s3) // 3) < 60:
        return "F"
#5
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"
