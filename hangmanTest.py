# Hangman challage from book 'SelfTaught' modified by Sami
# Coded on 27 March 2020 #stayathome
import random
import math

# random machinee yeaaah!!
def randAnimal():
    kakiempat = ['kuda', 'kucing',
                'anjing', 'sapi', 'domba', 'keledai',
                'kerbau', 'kelinci']
    kakidua = ['ayam', 'bebek', 'kanguru', 'burung']

    randnum = random.randint(0, len(kakiempat) - 1)
    randnum2 = random.randint(0, len(kakidua) - 1)

    hewan = [kakiempat[randnum],
            kakidua[randnum2]]

    randnum3 = random.randint(0, len(hewan) - 1)

    if randnum3 == 0:
        kwords = print("Kuncinya hewan domestik berkaki 4 :)")
    else:
        kwords = print("Kuncinya hewan domestik berkaki 2 :)")
        
    word = hewan[randnum3]
    return word

# intro coy
def starts():
    print('\nHaloo, ayo main Hang Man! *by python')
    print(
         "________ \n",
         "|   | \n",
         "|   0\n",
         "|  /|\ \n",
         "|  / \ \n",
         "| \n",
         "|______\n")
    
    gass = input('Yuk main yuk!\nJawab \'no\' untuk keluar\n')
    if gass != 'no':
        print('\nSilahkan tebak nama hewan domestik ya! kamu punya 7 kesempatan salah!')
        HangMan()
    else:
        print('\nOkayy, silahkan dicoba kembali lain waktu\nTerima Kasih !')
        quit

# maincode
def HangMan():
    stage = 0
    # chances
    wrong_gs = ["",
             "________ ",
             "|   | ",
             "|   0",
             "|  /|\ ",
             "|  / \ ",
             "| ",
             "| "]
    
    word = randAnimal()
    wordsLft = list(word)
    score_brd = [' _ '] * len(word)
    win = False
    print(''.join(score_brd))

    # Loop question
    while stage < len(wrong_gs) - 1:
        print('\n')
        guess = input('Masukan Huruf :')
        # if guess in word:
        if guess in wordsLft:
            char_index = wordsLft.index(guess)
            # score_brd[word.index(guess)] = guess
            score_brd[char_index] = guess
            wordsLft[char_index] = '$'
        else:
            stage += 1

        print(''.join(score_brd).upper())
        print('\n'.join(wrong_gs[0:stage + 1]))

        if ' _ ' not in score_brd:
            print('\nYesss kamu menang!')
            win = True
            break
    
    # closing
    if not win:
        # print('\n'.join(wrong_gs[0:stage]))
        print('\nMaaf kamu kalah! Jawabannya adalah: ')
        print(word.upper())
    
    print('\nTerima kasih, apakah kamu masih ingin bermain lagi?')
    
    again = input('Ketik \'yes\' untuk lanjut atau apapun untuk keluar:\n')
    if again != 'no':
        print('\nAyo bermain lagi!\n')
        HangMan()
    else:
        quit
    
starts()