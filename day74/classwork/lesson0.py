# 1
import math
def get_participants(n):
    return math.ceil((1 + math.sqrt(8 * n + 1)) / 2) if n > 0 else 0

# 2
def good_vs_evil(good, evil):
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]
    
    good_total = sum([i * b for i,b in zip(map(int,good.split()), good_worth)])
    evil_total = sum([i * b for i,b in zip(map(int,evil.split()), evil_worth)])
    
    
    if good_total > evil_total:
        return "Battle Result: Good triumphs over Evil"
    elif evil_total > good_total:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
    
# 3
def delete_nth(o,m):
    ll = o[::-1]
    for _ in range(100):
        for i in ll:
            while ll.count(i) > m:
                ll.remove(i)
    return ll[::-1]