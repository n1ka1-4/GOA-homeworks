#1
def count_positives_sum_negatives(arr):
    d = 0
    b = 0
    list1 = []
    if arr == []:
        return []
    else:
        for i in arr:
            if i > 0:
                b += 1
            else:
                d += i
        list1.append(b)
        list1.append(d)
        return list1
#2
def dna_to_rna(dna):
    return dna.replace("T","U")
#3
def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left
#4
def bmi(weight, height):
    bmi = weight / pow(height,2)
    if bmi <= 18.5: 
        return "Underweight"

    elif bmi <= 25.0: 
        return "Normal"

    elif bmi <= 30.0:
        return "Overweight"

    elif bmi > 30: 
        return "Obese"
#5
def minimum(lst):
    return min(lst)
def maximum(lst):
    return max(lst)
