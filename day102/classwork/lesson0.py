# 1
def is_vow(inp):
    return [i if chr(i) not in ["a", "e", "i", "o", "u"] else chr(i) for i in inp]

# 2
def explode(arr):
    if type(arr[0]) == str and type(arr[1]) == str:
        return "Void!"
    sumer = sum([i for i in arr if not type(i) == str])
    return list(map(list,zip((arr * sumer)[::2],(arr * sumer)[1::2])))

# 3
def scrabble_score(st): 
    scores = {
    **dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1),
    **dict.fromkeys(['D', 'G'], 2),
    **dict.fromkeys(['B', 'C', 'M', 'P'], 3),
    **dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4),
    'K': 5,
    **dict.fromkeys(['J', 'X'], 8),
    **dict.fromkeys(['Q', 'Z'], 10)
}

    return sum(scores.get(i.upper(),0) for i in st)
