chance = ['-1',
          '-2', '-3', '-4', '-5']
stage = 0
kata = 'bebek'
print(kata)
list_kata = list(kata)
score_brd = [" _ "] * len(kata)
print(''.join(score_brd))

while stage < len(chance):
    guess = input('masukin :\n')
    for i in range(len(guess)):
        list_guess = list(guess)
        indexing = list_guess[i]
        if guess == 'quit':
            break
        elif indexing in list_kata:
            char_index = list_kata.index(indexing)
            score_brd[char_index] = indexing
            list_kata[char_index] = '$'
        else:
            print('salah')
            stage += 1

    print(''.join(score_brd).upper())

    if ' _ ' not in score_brd:
        print('Yess, kamu menang!!')
        break
    # else:
    #     print('ini')
    #     print('\n'.join(chance[0: stage + 1]))
