#1
def get_count(s):
    return len([i for i in s if i in "aeiou"])
#2
def disemvowel(string_):
    string = [i for i in string_ if i.upper() != "A" and i.upper() != "E" and i.upper() != "I" and i.upper() != "O" and i.upper() != "U"]
    return "".join(string)
#3
def square_digits(num):
    srt1 = ""
    for i in str(num):
        srt1 += str(pow(int(i), 2))
    return int(srt1)