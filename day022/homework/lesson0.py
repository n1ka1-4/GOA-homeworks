def discount(x):
    if x < 18 and x > 0:
        return "you got discount"
    else:
        return "you didn't get discount"

print(discount(-21))
print(discount(23))
print(discount(16))