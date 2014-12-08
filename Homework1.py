import random

guesses=0

print('Hello! What is your name?')
myName = input()

print('Hello ' +myName+ '. Let\'s play a game.')
print('Think of a number between 1 and 100, and I\'ll try to guess it!')

def GuessGame():

    guess=50
    counter=25
    counter2=0

    print('Is it '+str(guess)+'? (yes/no)')
    answer=input()

    while(answer=='no'):
        counter2=counter2+1
        print('Is your number larger than '+str(guess)+'? (yes/no)')
        answer2=input()
    
        if(answer2=='yes'):
            guess=guess+counter
            counter=counter//2
        
        elif(answer2=='no'):
            guess=guess-counter
            counter=counter//2
        
        print('Is it '+str(guess)+'? (yes/no)')
        answer=input()
            
    else:
        print('I got it in '+str(counter2)+' tries!')
        print('Would you like to play again?')
        again=input()
        if(again=='yes'):
            GuessGame()
        if(again=='no'):
            print('Have a good day.')
            
        
GuessGame()
