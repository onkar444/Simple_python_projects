from IPython.display import clear_output
def greeting():
    
    print('\nGood Morning!!')
    print('\nWelcome to daily HOROSCOPE!')

    z='Zodiac Signs';
    print('\n',z.center(20,' '))
    print()

    print('1 : Aries')
    print('2 : Taurus')
    print('3 : Gemini')
    print('4 : Cancer')
    print('5 : Leo')
    print('6 : Virgo')
    print('7 : Libra')
    print('8 : Aries')
    print('9 : Sagittarius')
    print('10: Capricon')
    print('11: Aquarius')
    print('12: Pisces')

def horroscope(ch):
    
    if ch==1:
        print()
        print('ARIES:')
        print()
        print('''You have a beauitful day ahead. All the planets allign
such a way that it will help you feel energetic.
Your Lucky Number:3
Your Lucky Color: Red''')
        
    elif ch==2:
        print()
        print('TAURUS:')
        print()
        print('''You might have a hard day at home or office.
But you will be above a lot of people in your emotional health.
Your Lucky Number:9
Your Lucky Color:Pink''')
        
    elif ch==3:
        print()
        print('GEMINI:')
        print()
        print('''You will have quite good day. Offer some prayers today.
Your Lucky Number:19
Your Lucky Color:Peach''')    
    
    elif ch==4:
        print()
        print('CANCER:')
        print()
        print('''You have to help others today. Keep your mind and soul positive.
Your Lucky Number:31
Your Lucky Color:White''') 
        
    elif ch==5:
        print()
        print('LEO:')
        print()
        print('''Today you have to control your speech. You should offer some help to others.
Your Lucky Number:1
Your Lucky Color:Green''')    

    elif ch==6:
        print()
        print('VIRGO:')
        print()
        print('''You will have quite good day. This day will give you some good news.
Be grateful for today.
Your Lucky Number:19
Your Lucky Color:Blue''')    

    elif ch==7:
        print()
        print('LIBRA:')
        print()
        print('''Today is a normal day for you. Read some books.
Your Lucky Number:6
Your Lucky Color:Sky-blue''') 
    
    elif ch==8:
        print()
        print('SCORPIO:')
        print()
        print('''You will have quite good day. You have possiblity of getting some money today.
Your Lucky Number:4
Your Lucky Color:Brown''')    

    elif ch==9:
        print()
        print('SAGITTARIUS:')
        print()
        print('''You will have a normal day. You need to exercise today to keep your mind calm.
Your Lucky Number:3
Your Lucky Color:Yellow''')    
    
    elif ch==10:
        print()
        print('CAPRICON:')
        print()
        print('''You need to consult the doctor today. You might need to take regular check up.
Your Lucky Number:2
Your Lucky Color:Orange''')    

    elif ch==11:
        print()
        print('AQUARIUS:')
        print()
        print('''You need to read books today. The day will be some boring.
Your Lucky Number:3
Your Lucky Color:White''') 
    
    elif ch==12:
        print()
        print('PICES:')
        print()
        print('''You need to read books today. The day will be some boring.
Your Lucky Number:15
Your Lucky Color:Indigo''') 

def choice():
    ch=0
    while ch not in [1,2,3,4,5,6,7,8,9,10,11,12]:
        try:
            ch=int(input('\nEnter your zodiac sign:'))
        except:
            print('\nEnter valid zoidiac sign')
    return ch
    

               
               
while True:
    greeting()
    
    ch=choice();
    
    horroscope(ch)
    
    x=str(input('\nWant to know other zodiac? Enter Y/N:')).lower()
    if x[0]=='y':
        clear_output()
    elif x[0]=='n':
        clear_output()
        break

print('\nHave a NICE DAY!!!')
    
