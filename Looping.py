import sys
# for
huruf = input('Masukan huruf untuk di eja: ')
for i in huruf:
    if i == 'a':
        print('Ini blok Break')
        break
    if i == 'b':
        print('Ini blok Continue')
        continue
    if i == 'c':
        pass
        print('Ini blok Pass')
    print('Huruf ejaan: {}'.format(i))

print('')
print('Item hedonisme: ')
hedon = ['Nmax', 'Apple', 'Nike', 'Swiss Army']
for index in range(len(hedon)):
    print('Bisa {}'.format(hedon[index]))

# loop each char
for x in input(''):
    print(x)

# while
print('')
hitung = 0
while (hitung < 5):
    print('Hitungan ke-{}'.format(hitung))
    hitung = hitung + 1

# nested loop
for z in range(0, 5):
    for j in range(0, 5 - z):
        print('*', end='')
    print()

# else after for
for item in huruf:
    # i adalah rantaian huruf pada for diatas
    if i == 'a':
        print('Ada huruf \'A\' nya!')
        break
else:
    print('Tidak ada huruf \'A\' nya!')

# else after while
y = 5
while y > 0:
    y = y - 1
    if y == 2:
        print("Sudah ke angka {} Loop selesai!".format(y))
        break
    print(y)
else:
    print("Loop selesai!")

# catch exception using pass blok
data = ''
while (data != 'x'):
    try:
        data = input('Masukan integer (ketik \'x\' untuk keluar): ')
        print('integernya: {}'.format(int(data)))
    except:
        if data == 'x':
            pass
            print('menjalankan blok pass yaitu keluar')
        else:
            print('error: {}'.format(sys.exc_info()[0]))

# filling list using loops
num = [1, 2, 3, 4]
kotak = []
print('kotak sebelum loop: ', kotak)

for n in num:
    kotak.append(n ** 2)

kotak2 = [n ** 2 for n in num]

print('kotak sesudah loop: ', kotak)
# simplified
print('kotak sesudah loop v2: ', kotak2)

# kesamaan dalam 2 list
listA = [1, 2, 3, 4, 5, 6]
listB = [2, 3, 4, 5, 6, 7, 8]

kotak = []
for a in listA:
    for b in listB:
        if a == b:
            kotak.append(a)
# simplified
kotak2 = [a for a in listA for b in listB if a == b]

print(kotak)
print(kotak2)

# lower semua isi list
lowerListHedon = [_.lower() for _ in hedon]
print(lowerListHedon)

# test
listA = range(1, 10, 2)
x = [[a ** 2, a ** 3] for a in listA]
print(x)
# [[1, 1], [9, 27], [25, 125], [49, 343], [81, 729]]