def summ(*arg):
    try:
        return sum(list(arg))
    except TypeError:
        return "TypeError: list contains (str)"


print(summ(1,2,3,5,"1"))