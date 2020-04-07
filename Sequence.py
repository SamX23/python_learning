# List
l = [12, 2, 10, 4, 3]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l = ['b', 'c', 'a', 'B', 'C', 'A']
l.sort(key=str.lower)
print(l)

# Tuple
t = (1, 2, 3, 4, 5)

y = "string"
print(y[1])
print(y)

xx = [2] * 6
print(xx)

# slicing
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(len(x))
print(x[5])
print(x[-1])
print(x[2:7])
print(x[:5])
print(x[-3:])
print(x[1:7:2])

x[3] = 0
print(x)
x.append(55)
print(x)
del x[8]
print(x)

# tuple
z = (2, 'test', 2 + 3j)
print(z[1])
print(z[0:3])

# set
a = {2, 2, 2, 3, 3, 4, 4, 5}
print(a)

# dictionary ( value:key )
b = {1: 'value', 'key': 2, 'value': 'key'}
print(type(b))
print(b[1])
print(b['key'])
print(b)

# Konvert / konversi
float(5)
int(10.6)
float('2.6')
str(2.5)

set([1, 2, 3])
tuple({3, 4, 5})
list('haiii')
dict([[1, 2], [3, 4]])

# range
for bebas in range(9):
    print(bebas)
for bebas in range(3, 9):
    print(bebas)

[_ for _ in range(1, 9, 2)]  # list comprehension

listing = ['satu', 'dua', 'tiga']
print('empat' in listing)
print('empat' not in listing)

# variable assignment
mobil = ['kuning', '2000 CC', 'Pertamax Turb', 2020]
Color, engine, bensin, pembuatan = mobil
print(Color, pembuatan)
