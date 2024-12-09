def manual_in(num, li):
    i = 0
    while i < len(li):
        if li[i] == num:
            return True
        else:
            i += 1
    if i == len(li):
        return False
print(manual_in(4, [1, 2, 3,4, 5]))
