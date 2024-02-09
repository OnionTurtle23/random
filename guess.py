import random
import math
print("Let's play a guessing game")
print("Define a range of whole numbers and I will select one within that range.\n Then you try to guess my number using the fewest guesses!")
x = int(input("Please enter a whole number: "))
y = int(input("Please enter another whole number: "))
z = random.randint(x , y)
print(z)
gCount = 0

def guess ():
    g = int(input("Pick a number between " + str(x) + " and " + str(y) + ": "))

guess()

def evaluate (guess, z, gCount):
        if guess > z:
            print("Good guess, but too high! Try again.")
            gCount += 1 
        elif guess < z:
            print("Oops, too low this time. Please try again")
            gCount += 1
        else:
            print("Nice! You guessed my number in " + str(gCount) + " guesses!")
        
        guess()


while guess != z:
    evaluate(guess, z, gCount)