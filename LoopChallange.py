# Created by Sami at 24/04/2020
# samx23.github.com
import random

print('Ketik \'q\' untuk keluar', '\n',
      'Ketik \'random\' untuk menggunakan angka random', '\n',
      'Atau ketik \'angka\' sebagai trigger tebakannya!', '\n',
      'lalu tebak angka tersebut!')


# choice
class Kirakira:
    def __init__(self):
        super().__init__()

    def choice(self):
        if self == 'random':
            dari = int(input('Dari : '))
            sampai = int(input('Sampai : '))
            # if type(dari) and type(sampai) == str:
            #     return 'q'
            return Kirakira.rand(dari, sampai)
        elif self == 'angka':
            return input('Masukan angka biasa: ')
        else:
            return 'err'

    def rand(dari, sampai):
        res = random.randint(dari, sampai)
        return res


# main code

while True:
    tanya = input('Menggunakan random atau angka biasa? ')
    guess = Kirakira.choice(tanya)

    if tanya == 'q':
        print('Terima kasih, silahkan coba lagi nanti!\nExit\n')
        break
    elif guess == 'q':
        print('Terima kasih, silahkan coba lagi nanti!\nExit \n')
        break
    elif guess == 'err':
        print('\nHanya input \'random\', \'angka\' dan \'q\'.\nSilahkan dicoba kembali!')
        break

    errCnt = 0

    # Guesser
    while True:
        tebak = input('Tebak angka : ')
        errCnt += 1

        if tebak == 'q':
            print('Exit \n')
            break
        elif int(tebak) == guess:
            print('Mantaapp Benar! \n')
            break

        elif tebak == str(guess):
            print('Mantaapp Benar! \n')
            break
        else:
            print('Salah cuy! \n')

            if errCnt == 3:
                print('Masih salah, dicoba lagi\n')

            elif errCnt == 5:
                print('Yang benar adalah: ', guess, '\n')
                errCnt = 0
                break

    print('Silahkan masukan pilihan untuk memulai kembali \n \n')

# Write a program that has an infinite loop (with q to quit),
# and each time through the loop, it asks the user to guess
# a number and tells them whether their guess was right or wrong.
