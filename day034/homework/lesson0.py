def manual_min(lst):
    if len(lst) == 0:
        return None
    min_value = lst[0]
    for value in lst:
        if value < min_value:
            min_value = value
    return min_value

def manual_max(lst):
    if len(lst) == 0:
        return None
    max_value = lst[0]
    for value in lst:
        if value > max_value:
            max_value = value
    return max_value

