# Angka int to str
x = 1
print(str(x).zfill(4))

y = 'Sami Kalammallah'
print(y.upper())
print(y.lower())
print(y.isupper())
print(y.islower())

# \'          Single quote
# \"          Double quote
# \t          Tab
# \n         Newline (line break)
# \\          Backslash
print("bismillah, ini adalah \'testing\' untuk kode \\\\ comment \ndan ini adalah new line")
print(r"ini teks sesuai format \\ ', ! dan \n sebagainya")
mLine ="""hoi!
wassap?
ini test."""
print(mLine)

# isX dari String untuk pengecekan
while True:
    print('Masukan Usia : ')
    age = input()
    if age.isdecimal():
        break
    print('Tolong masukan angka.')

while True:
    print('Buat Password : ')
    password = input()
    if password.isalnum():
        break
    print('Password hanya dapat berisi nama dan angka.')

# validasi .startswith dan .endwith dari String
while True:
    validate = input('Masukan password : ')
    if validate.startswith(password):
        print('Password Benar!')
        break
    print('Password Salah!')

# join and split String
Mobil = ' dan '.join(['Roda', 'Lampu', 'Knalpot', 'Mesin'])
print('Komponen Mobil terdiri dari '+Mobil)
print(Mobil.split('dan'))

z = 'testing'
print(z.center(15, '-'))
print(z.rjust(15))
print(z.strip())
zx = 'sami dan sami dan sami ke 3 itu samis itu samix'
print(zx.replace('sami', 'ganti', 2))
