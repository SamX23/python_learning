# Create a text based game of favorite sport
# make up a text based dialogue game
# make a program about kind of mood and recommend a song
# build a program using brands and trademark, a text based
# program about mood and recommend a solution


def program():
    goodMood = ['happy', 'gracious', 'great']
    neutralMood = ['shy', 'confused', 'meh']
    badMood = ['bad', 'anxious', 'cry']

    print("____________________________________________\n"
          'Hello, welcome to mood helper app\n'
          'Where you can tell us your mood today and\n'
          'we help you by giving you a suggestion!')

    while True:
        inp = input('\nTell us your mood: ')
        if inp in goodMood:
            print('Nice, keep readin Qur\'an')
        elif inp in neutralMood:
            print('Try to read Qur\'an more')
        elif inp in badMood:
            print('Be calm, learn what is Islam')
        elif inp == 'q':
            print('Quit!')
            break
        else:
            print('nope')


program()
