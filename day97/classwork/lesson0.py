# 1
def move_zeros(lst):
    return [i for i in lst if i != 0] + [0 for i in range(lst.count(0))]

# 2
def generate_hashtag(s):
    title = "".join(s.title().split())
    return "#" + title if 0 < len(title) < 140 else False

# 3
import string
def pig_it(text):
    return " ".join([i[1:] + i[0] + "ay" if i.isalpha() else i for i in text.split()])

# 4
def rot13(message):
    t = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    return message.translate(t)

# 5
def dir_reduc(arr):
    dict1 = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    ll = []
    for i in arr:
        if ll and dict1[i] == ll[-1]:
            ll.pop()
        else:
            ll.append(i)
    return ll

# 6 
def domain_name(url):
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    url = url[:url.rfind(".")]
    if url.startswith("www."):
        url = url[4:]
    while True:
        if url.count(".") != 0:
            url = url[:url.rfind(".")]
        else:
            break
    return url
