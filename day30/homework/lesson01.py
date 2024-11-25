def manual_replace(a,replaceed,replaceer):
    for i in a:
        if i == replaceed:
            a[a.index(i)] = replaceer
    return a

