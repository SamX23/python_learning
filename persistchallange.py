# use files to persist data by writing the output of programs to a file
# write a program that collects data from a user and saves it
# to a file, so the data persist

import csv
    
class WriteFiles:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr
        print(name, age, addr)
        with open('files.txt', 'w') as files:
            files.write('Name: ')
            files.write(name)
            files.write('\n')
            files.write('Age: ')
            files.write(age)
            files.write('\n')
            files.write('Address: ')
            files.write(addr)

print('Welcome to our self input saving program.\n'
        'Please input your name, your age and your address!\n \n'
        'Press \'n\' to quit.\n')

while True:
    perm = input('Do you want to proceed? \'y\' or \'n\'\n ')
    if perm == 'n':
        break
    else:
        name = input('Your name: ')
        age = input('Your age: ')
        addr = input('Your address: ')
        break
    
WriteFiles(name, age, addr)