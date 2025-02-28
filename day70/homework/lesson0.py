# 1
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

# 2
def unique_in_order(s):
    if len(s) == 0:
        return []
    else:
        res = s[0]
        ll = [s[0]]

        for i in s:
            if res != i:
                ll.append(i)
                res = i
        return ll
        
# 3
def binary_array_to_number(arr):
    return int(f'0b{"".join(map(str, arr))}', 2)

# 4
def expanded_form(num):
    res = []
    for i in range(len(str(num))):
        if str(num)[i] != '0':
            res.append(str(num)[i] + "0" * (len(str(num)) - i - 1))
    return " + ".join(res)

# 5
def is_valid_IP(strng):
    if strng.count(".") != 3:
        return False
    else:
        for i in strng.split("."):
            if not i.isdigit():
                return False
            
            elif int(i) > 255 or int(i) < 0:
                return False
            
            elif i[0] == "0" and len(i) > 1:
                return False
    
        else:
            return True