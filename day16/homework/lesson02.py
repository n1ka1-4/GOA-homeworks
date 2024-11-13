person1 = int(input("enter your score: "))
if person1 > 90 and person1 < 100:
    print("Grade A")
elif person1 > 70 and person1 < 79:
    print("Grade B")
elif person1 > 60 and person1 < 69:
    print("Grade C")
elif person1 > 50 and person1 < 59:
    print("Grade D")
elif person1 < 49:
    print("Grade F")
else:
    print("score is out of range")
