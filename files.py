import csv

# writing files
files_me = open('test.txt', 'w')
files_me.write('Written by python man!')
files_me.close

with open('test2.txt', 'w') as files2: files2.write('New file with automatic close command')

# reading files then input into list
tList = list()
with open('test2.txt', 'r') as files2:
    for line in files2.read():
        tList.append(line)

print(tList)

# writing with CSV
with open('csvtest.csv', 'w') as files3:
    writter = csv.writer(files3, delimiter = ',')
    writter.writerow(['Name', 'Address', 'phone'])
    writter.writerow(['Sami', 'Cianjur', '089657511134'])

# writing with CSV
with open('csvtest.csv', 'r') as files3:
    reader = csv.reader(files3, delimiter=',')
    for row in reader:
        print(','.join(row))