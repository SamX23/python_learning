import time
import sys
from random import randrange

class rText():
    def __init__(self, input,
                    tm='0.1'):
        # print('Running Text!')
        # text = input
        sec = tm + str(randrange(1, 4, 1))
        sec = float(sec)
        
        for x in input:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(sec)

class dText():
    def __init__(self, text,
                    delay = 2, count = 4):
        x = 0
        while x < count:
            print(text)
            time.sleep(delay)
            x += 1