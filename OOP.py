# oop program learning

class Human:
    def __init__(self, fname, lname, address):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.fullname = fname + ' ' + lname
        self.email = lname + '.' + fname + '@' + 'email.com'

hmn_1 = Human('doni', 'husnan', 'bandung')

print(hmn_1.fullname)