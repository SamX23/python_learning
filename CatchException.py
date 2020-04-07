x = {'totol': '20.0'}
try:
    print('Rata-rata: {}'.format(x['to_tol']))
except KeyError:
    print('Kunci tidak ada pada x')
except ValueError:
    print('Nilai tidak sesuai')

try:
    print('Rata-rata: {}'.format(x['totol'] / 3))
except KeyError:
    print('Kunci tidak ada pada x')
except (ValueError, TypeError):
    print('Nilai atau tipe tidak sesuai')

try:
    print('Pembulatan rata-rata: {}'.format(int(x['totol'])))
except (ValueError, TypeError) as e:
    print('Penanganan kesalahan: {}'.format(e))

# menghasilkan pengecualian
if 'total' not in x:
    raise KeyError('Harus ada total pada dictionary!')
