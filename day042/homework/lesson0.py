#1
def solution(text, ending):
    return text.endswith(ending)
#2
def accum(st):
    b = 1  
    s = "" 
    f = [] 
    for i in st:
        s = i * b
        f.append(s.capitalize())
        b += 1
    return "-".join(f)
#3
def DNA_strand(dna):
    new_dna = ""
    for i in dna:
        if i == "A":
            new_dna += "T"
        elif i == "T":
            new_dna += "A"
        if i == "G":
            new_dna += "C"
        elif i == "C":
            new_dna += "G"
    return new_dna
#4
def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]
#5
def get_sum(a,b):
    res = 0
    if a < b:
        for i in range(a,b+1):
            res += i
    else:
        for i in range(b,a+1):
            res += i
    return res