# Eli Gibbs
# 5/6/2022
# Score list

import random

name = input("Hello what is your name?")
number = random.randint(1,100)
print("Hi " + name + ", Please pick a number between 1 and 100.")
guessesTaken = 0

while guessesTaken < 5:
    guess = int("Enter a guess: ")
    guess = int(guess)
    if guess < number:
        print("That was too low.")
    elif guess > number:
        print("That was too high!")
    else:
        break

 if guess == number:
    print("Winner winner, chicken dinner! Congrats " + name + " you guessed the correct number!")
 else:
     print("You lose, too bad. better luck next time. The right number was", number)
    
