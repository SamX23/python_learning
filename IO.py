import sys
# %s - String
# %d - Integers
# %f - Pecahan
# %.<digit>f - Bilangan pecahan dengan sejumlah digit angka dibelakang koma.
# %x/ %X - Bilangan bulat dalam representasi Hexa (huruf kecil/huruf besar)

print('Bismillah, {}'.format('Gan!!'))
name = input("Nama : ")
num = input("Usia : ")
age = int(num)
print(type(age))

print("Hola, %s!" % name)
print('Usia %s adalah %d tahun!' % (name, age))