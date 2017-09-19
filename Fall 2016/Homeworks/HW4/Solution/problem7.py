import random

# Obtain the random number 0 or 1
number = random.randint(0, 1)

# Prompt the user to enter a guess
guess = int(input("Enter 0 for Head and 1 for Tail: "))

# Check the guess
if guess == number:
    print("You guessed correctly!")
elif number == 0:
    print("Sorry, it is a head.")
else:
    print("Sorry, it is a tail.")
