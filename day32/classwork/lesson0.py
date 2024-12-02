#1
def abbrev_name(name):
    return name[0].upper() + "." + name[name.find(" ")+1].upper()

#2
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

#3
def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9

#4
def find_needle(haystack):
    x = haystack.index("needle")
    return f"found the needle at position {x}"

#5
def invert(lst):
    lis1 = []
    if lst == []:
        return []
    else:
        for i in lst:
            lis1.append(i * -1)
    return lis1
        
        