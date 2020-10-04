#This is the display function"""
import random
import os
from IPython.display import clear_output

#This is to display the heading of the game
def displayGame():
    print()
    print('Welcome to the Game!!!')
    print()
    s='ROCK PAPER SCISSOR GAME'
    print(s.center(40,' '))
    

#This is the code to generate computer's hand   
def computer_hand():
    
    c_hand=random.randint(1,3)
    
    return c_hand


#This is to return the computer's hand 
def com_hand():
    
    ch=computer_hand()
    
    if ch==1:
        return ('rock')
    
    elif ch==2:
        return ('paper')
    
    elif ch==3:
        return ('scissors')
        

        
#This is the function to accept the user input
def user_input():
    print()
    print('1. ROCK')
    print('2. PAPER')
    print('3. SCISSORS')
    print()
    user_choice=0
    while user_choice not in [1,2,3]:
        try:
            user_choice=int(input('Enter your choice:'))
        except:
            print('ENTER VALID INPUT!!!')
        
    
    if user_choice==1:
        user_choice='rock'
        
    elif user_choice==2:
        user_choice='paper'
        
    elif user_choice==3:
        user_choice='scissors'
        
    return user_choice

#This is our game's logic
def game_logic(name):
    
    
    computer=com_hand()
    #print(computer)
    user=user_input()
    
    print()
    if computer=='paper' and user == 'rock':
        print('Computer::{} : User::{}'.format(computer,user))
        print()
        print('Computer Wins!!!')
   
    elif computer=='rock' and user == 'scissors':
        print('Computer Wins!!!')
        print()

        print('Computer::{} : User::{}'.format(computer,user))
    
    elif computer=='scissors' and user == 'paper':
        print('Computer Wins!!!')
        print()

        print('Computer::{} :User::{}'.format(computer,user))

    elif user=='paper' and computer=='rock':
        print('{} wins!!!'.format(name))
        print()
        print('User::{} : Computer::{}'.format(user,computer))
        
    elif user=='rock' and computer=='scissors':
        print('{} wins!!!'.format(name))
        print()
        print('User::{} : Computer::{}'.format(user,computer))

        
    elif user=='scissors' and computer=='paper':
        print('{} wins!!!'.format(name))
        print()
        print('User::{} : Computer::{}'.format(user,computer))

        
    else:
        print("Game Tie!!")
        print()
        print('User::{} : Computer::{}'.format(user,computer))

        
    
################ MAIN CODE ########################    

if __name__=='__main__':
    clear_output()
    
    name=str(input('Enter your name:'))
    game=True
        
    while game:
        displayGame()
        #clear_output()
        
        game_logic(name)
        ch=''
        while ch not in ['y','n','yes','YES','Y','NO','no','No']:
            ch=str(input('\nWant to play another game ? Enter Y/N:'))
            
            
        
        if ch[0]=='y':
            #clear_output()
            os.system('cls')
            
        else:
            if ch[0]=='n':
                #clear_output()
                break 
           
            
    
