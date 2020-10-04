 import random
import os
from IPython.display import clear_output


number=random.randint(0,100)
game='on'
check=True
points=100;
name=input('Enter your good name:')
chances=10;
while game=='on':
    #os.system('cls')
    clear_output()
    print('Welcome to NuMbEr GuEsS GaMe!\n')
    print('For each guess you will lose 10 points!')
    print('You have to guess the number in 10 chances!')
    print('\nLets Begin!!!')
    while chances>0:
        #os.system('cls')
        #clear_output()
        print('{} you have {} chances!'.format(name,chances))
        player_input = (input('Enter your GuEsS:'))
        try:
            val=int(player_input)
        except:
            print('This is not a valid guess!, Please Try again!')
            continue
        val=int(player_input)
        if val < number:
                print('Your are close, but less than NUMBER!')
                

        elif val > number:
                print('Your are close, but greater than NUMBER!')

        elif val == number:
            print('Your are right!!!\n')
            break
        chances-=1
        points-=10
    print('You Won the game with {} points!!!'.format(points))
    ch=input('You want to play another game?,\nEnter yes if not Enter no!')
    ch=ch.lower()
    if ch[0] == 'y':
        game='on'
        chances=10
    else:
        game='off'
print('Thank You! for playing the game!')
print('Have a nice day!')
