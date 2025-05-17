# 1
websites.append("codewars")

# 2
def quadrant(x, y):
    return 1 if x > 0 and y > 0 else 2 if x < 0 and y > 0 else 4 if x > 0 and y < 0 else 3

# 3
def lowercase_count(strng):
    return len(strng) - len(strng.translate(str.maketrans("", "", "aqzxswedcvfrtgbhynujmkiolp")))

# 4
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        if self.draft - self.crew * 1.5 >= 20:
            return True
        else:
            return False
        
# 5
def converter(mpg):
    return round(mpg * 0.3540060435382138, 2)

# 6
def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))

# 7
import math
def square_area(a):
    return round(((a*4 / math.pi) / 2) ** 2,2)

# 8
class Solution:
    
    @staticmethod
    def main(self, *args):
        print("Hello World!")

# 9
def subtract_sum(n):
    dict1 = {
1:"kiwi",
2:"pear",
3:"kiwi",
4:"banana",
5:"melon",
6:"banana",
7:"melon",
8:"pineapple",
9:"apple",
10:"apple",
11:"cucumber",
12:"pineapple",
13:"cucumber",
14:"orange",
15:"grape",
16:"orange",
17:"grape",
18:"apple",
19:"grape",
20:"cherry",
21:"pear",
22:"cherry",
23:"pear",
24:"kiwi",
25:"banana",
26:"kiwi",
27:"apple",
28:"melon",
29:"banana",
30:"melon",
31:"pineapple",
32:"melon",
33:"pineapple",
34:"cucumber",
35:"orange",
36:"apple",
37:"orange",
38:"grape",
39:"orange",
40:"grape",
41:"cherry",
42:"pear",
43:"cherry",
44:"pear",
45:"apple",
46:"pear",
47:"kiwi",
48:"banana",
49:"kiwi",
50:"banana",
51:"melon",
52:"pineapple",
53:"melon",
54:"apple",
55:"cucumber",
56:"pineapple",
57:"cucumber",
58:"orange",
59:"cucumber",
60:"orange",
61:"grape",
62:"cherry",
63:"apple",
64:"cherry",
65:"pear",
66:"cherry",
67:"pear",
68:"kiwi",
69:"pear",
70:"kiwi",
71:"banana",
72:"apple",
73:"banana",
74:"melon",
75:"pineapple",
76:"melon",
77:"pineapple",
78:"cucumber",
79:"pineapple",
80:"cucumber",
81:"apple",
82:"grape",
83:"orange",
84:"grape",
85:"cherry",
86:"grape",
87:"cherry",
88:"pear",
89:"cherry",
90:"apple",
91:"kiwi",
92:"banana",
93:"kiwi",
94:"banana",
95:"melon",
96:"banana",
97:"melon",
98:"pineapple",
99:"apple",
100:"pineapple"
}
    while n not in dict1:
        n -= sum(int(i) for i in str(n))
    return dict1[n]

# 10
def billboard(name, price=30):
    return sum(price for i in range(len(name)))

# 11
from random import choice

class Ghost(object):
    def __init__(self):
        self.color = choice(["white", "yellow", "purple", "red"])

# 12
def to_csv_text(array):
    return '\n'.join(','.join(map(str, row)) for row in array)

# 13
def contamination(text, char):
    return "".join(char for _ in text)

# 14
def sp_eng(sentence): 
    return "english" in sentence.lower()

# 15
class Human:
    pass
class Man(Human):
    pass
        
class Woman(Human):
    pass

def God():
    return [Man(), Woman()]
