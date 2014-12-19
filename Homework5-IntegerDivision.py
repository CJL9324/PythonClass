from random import randrange

def check(answer,test):
    if answer == int(test):
        print("Brilliant, You're right!")
    else:
        print ("Incorrect. You'll get better with practice!!! The correct answer was",int(test))

 
    
choice = "y"

while (choice=="y"):
    
    a = randrange(10)
    b = randrange(10)
    
    try:
        test = (a/b)
    except ZeroDivisionError: 
        pass
    try:
        if int(test)==float(test):
            answer = input (str(a)+"/"+str(b)+"=")
            answer = int(answer)
            check(answer, test)
            
            choice =input("Play again? (y/n)   ")
            if(choice=="n"):
                print("Thanks for playing! Keep Practicing.")

    except ValueError:
        print("Please enter integers only!")