def displayme(str):
    print(str)

ex = input('apapun: ')
displayme(ex)

# Return func
def sum(arg1, arg2):
    total = arg1 + arg2
    print('Ini ada didalam fungsi: {}'.format(total))
    return total

def kuadrat(x):
    return x*x

ex = sum(2, 2)
print('Ini ada diluar fungsi: {}'.format(ex))

x = 12
ex = kuadrat(x)
print('Kuadrat dari {} adalah {}'.format(x, ex))

# Pass by ref vs value
def changeme(xlist):
    xlist.append([1, 2, 2, 4])
    print('List dalam fungsi: {}'.format(xlist))

xlist = [0, 1, 3, 4]
changeme(xlist)
print('List dilaur fungsi: {}'.format(xlist))

# func with default arg
def cetak(name, age=10):
    print('Nama: ', name)
    print('Usia: ', age)

cetak('Sami', 24)
cetak('Rifka')