# codewars
def solution(number):
    return sum([ i for i in range(1, number) if i % 3 == 0 or i % 5 == 0])

greet = lambda : "hello world"
sum1 = lambda a, b: a + b

print(greet())
print(sum1(2,4))