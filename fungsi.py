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

# variable-length arguments
def funcname(fixedArg, *args):
    print('arg posisi {}'.format(fixedArg))
    for a in args:
        print('arg tambahan {}'.format(a))

funcname(10)
funcname(20, 70, 12)

# variable-dinamic arguments
def printout(*args, **kwargs):
    for a in args:
        print('args posisi {}'.format(a))
    for key, value in kwargs.items():
        print('args kata kunci {}:{}'.format(key, value))

printout(1, 2, 3)
printout(a=2, b=3, c=4)
printout(1, 3, a=2, b=4)
printout(*(2, 3), **{'a': 1, 'b': 4})

# anonim func lambda
sum = lambda arg1, arg2: arg1 * arg2
print('sum of total : ', sum(20, 30))

# Variable Range
total = 0
def sum(arg1, arg2):
    global total
    total = arg1 + arg2
    print('Inside func: {}'.format(total))
    return total

total = sum(10, 20)
print('Outside func: {}'.format(total))
