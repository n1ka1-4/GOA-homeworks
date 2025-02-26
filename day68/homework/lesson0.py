def speedify(st):
    ll = [" "] * 100000
    
    for i,b in enumerate(st):
        ll[i + ord(b) - 65] = b
        
    return "".join(ll).rstrip()