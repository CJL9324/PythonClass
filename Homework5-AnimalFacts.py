class Animal:
    def __init__(self, name):
        self.name = name

    def guess_who_am_i(self):
        i = 1
        for hint in (game_dict[self.name]):
            print ("Hint "+str(i)+": "+hint)
            answer = input ("Who am I?")
            if answer.lower()== self.name:
                print ("You got it! I am a "+self.name)
                break
            else:
                print ("Nope. Here's another hint!\n")
                i +=1
            if i > 3:
                print("Sorry, I\'m out of hints.")
                print ("The answer was "+self.name)
            
game_dict = {"elephant": ["I have an exceptional memory", "I am the largest land-living mammal in the world", "I have a trunk"],
             "tiger":["I am the biggest cat", "I come in black and white, or orange and black", "I am a carnivore"],
             "bat":["I use echo-location", "I can fly", "I see well in the dark"]}
e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

print("Let's play a guessing game.")
print ("Guess the three different animals! I will give you three hints for each one.")

print ("\nGuess the first Animal:")
e.guess_who_am_i()
print ("\nGuess the second Animal:")
t.guess_who_am_i()
print ("\nGuess the third Animal:")
b.guess_who_am_i()

print("Thanks for playing!")