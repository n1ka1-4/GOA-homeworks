# 1
def combine_names(name, last):
    return name + " " + last

# 2
class Sleigh(object):
    def authenticate(self, name, password):
        if password == "Ho Ho Ho!" and name == "Santa Claus":
            return True
        else:
            return False
        
# 3
websites = ["codewars"] * 1000

# 4
def solution(digits):
    max1 = 0
    for i in range(len(digits)):
        if int(digits[i:i + 5]) > max1:
            max1 = int(digits[i:i + 5])
    return max1

# 5
def triangular(n):
  return n * (n + 1) // 2 if n > 0 else 0

# 6
def alphabet_position(text):
    return " ".join([str(ord(i.lower()) - 96) for i in text if i.lower() in "azqwsxcderfvbgtyhnujmkiolp"])
  