
from operator import *
x = 2 << 2
print(x)

a=1
b=5.0
print('a = ', a)
print('b = ', b)

# perbandingan
for func in (lt, le, eq, ne, ge, gt):
    print('%s(a, b): ' % func.__name__, func(a,b))

