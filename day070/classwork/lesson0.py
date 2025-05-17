# 1
def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])

# 2
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    
# 3
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