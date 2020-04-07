# if else elif
print("Penghitung diskon")
jmlh = int(input("Masukan uang: "))
if jmlh < 1000:
    diskon = jmlh * 0.05
    disc = int(diskon)
    print("Diskon: ", disc)
elif jmlh < 2500:
    diskon = jmlh * 0.10
    disc = int(diskon)
    print("Diskon: ", disc)
else:
    diskon = jmlh * 0.15
    disc = int(diskon)
    print("Diskon: ", disc)

total = jmlh - diskon
cnv = int(total)
print("Yang harus dibayar: ", cnv)

# ganjil genap
if cnv % 2 == 0:
    print('{} adalah genap'.format(cnv))
else:
    print('{} adalah ganjil'.format(cnv))

# Positif negatif
print("Check negatif atau positif")
x = int(input("Angka: "))
if x < 0:
    print('{} adalah negatif'.format(x))
elif x == 0:
    print('{} adalah nol'.format(x))
else:
    print('{} adalah positif'.format(x))

# Ternary operators (condition true if condition else condition false)
print('{} adalah negatif'.format(x) if x < 0 else '{} adalah positif'.format(x))
