# print(y.upper())
# print(y.lower())
# print(y.isupper())
# print(y.islower()

x = 'TuLiSaN AlAy'
y = ""
for i in x:
    if i.islower():
        y = y + i.upper()
    else:
        y = y + i.lower()

print(y)

s = 'Sami'


def swap_cs(s):
    a = ""
    for let in s:
        if let.isupper():
            # a += (let.lower())
            a = a + let.lower()
        else:
            a += (let.upper())
    return a


print(swap_cs(s))
