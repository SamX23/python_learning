# oop program learning

class Human:
    def __init__(self, fname, lname, address, job):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.job = job
        self.fullname = fname + ' ' + lname
        self.email = lname + '.' + fname + '@' + 'email.com'

password = input('Setup Password: ')
while True:
    validate = input('Masukan Password: ')
    if validate == password:
        print('Lanjut perkenalan..')
        break
    print('Password Salah!')

hmn_1 = Human('Sami', 'Kalammallah', 'Cianjur', 'ngoding')

print('Bismillah, hello world!')
print('Saya ' + hmn_1.fullname)
print('Tinggal di ' + hmn_1.address)
print('Alamat email saya ' + hmn_1.email.lower())
print('Kesibukan saat ini adalah ' + hmn_1.job)