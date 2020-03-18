y = "string"
print(y[1])
print(y)

# slicing
x = [5,10,15,20,25,30,35,40,45,50]
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
z = (2, 'test', 2+3j)
print(z[1])
print(z[0:3])

# set
a = {2, 2, 2, 3, 3, 4, 4, 5}
print(a)

# dictionary
