#!/usr/bin/env python3
try:
    print('If you provide a legal file name, this program will \
      output the last two lines of the song to that file...')
    print('\nMary had a little lamb,')
    answersnow = input('With fleece as white as (enter your file name): ')
    answersnowobj = open(answersnow, 'w')
#except:
#    print('Error with that file name!')
else:
    print('and everywhere that Mary went', file=answersnowobj)
    print('the lamb was sure to go', file=answersnowobj)
    answersnowobj.close()
finally:
    print('Thanks for playing!')
    quit()
