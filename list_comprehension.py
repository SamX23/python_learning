from math import pi

animal = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
animal2 = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')]
# 1st
na1 = []
for x in range(0, 7):
    na1.append(animal[x])
# 2nd
na2 = list(map(lambda i: animal[i], range(0, 7)))
# 3rd
na3 = [animal[i] for i in range(0, 7)]
print(na1, '\n', na2, '\n', na3)

vec = [-4, -2, 0, 2, 4]
print('value doubled')
print([x * 2 for x in vec])
print('filter negative number')
print([x for x in vec if x >= 0])
print('apply function abs() to all element')
print([abs(x) for x in vec])
print('create a list of 2 tuples (x, y)')
print([(x, x ** 2) for x in range(6)])
fresh = ['   banana', '   berry  ', 'fruit   ']
print('strip the space and call a method on each element')
print([weapon.strip() for weapon in fresh])
print('join of flatten a list using a listcomp with for')
ver = [[1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9, 10]]
print([num for elem in ver for num in elem])
print('list comprehension can include complex expression and nested function')
print([str(round(pi, i)) for i in range(0, 7)])

print('Versi Rieut')
x = 1
y = 1
z = 1
n = 2
ar = []
p = 0
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                ar.append([])
                ar[p] = [i, j, k]
                p += 1
print(ar)

print('Versi List comprhension edaan singkat')
ar = [[i, j, k] for i in range(x + 1)
      for j in range(y + 1)
      for k in range(z + 1)
      if i + j + k != n]
print(ar)
