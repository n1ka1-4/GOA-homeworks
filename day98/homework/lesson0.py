# 1
def rot13(message):
    t = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    return message.translate(t)

# 2
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

# 3
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

# 4
def to_underscore(strng: str) -> str:
    ll = []
    b = 0
    if isinstance(strng, int):
        return str(strng)
    for i in range(len(strng)):
        if strng[i].isupper() and i != 0:
            ll.append(strng[b:i])
            b = i
        if i == len(strng) - 2:
            ll.append(strng[b:])
    return "_".join(ll).lower()
            
# 5
import string
def alphanumeric(password):
    return all(i not in string.whitespace and i not in string.punctuation for i in password) and len(password) > 0