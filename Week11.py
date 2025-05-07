"""
This is a summary of what we did in week 11. Examples from the thinking tasks as well as others from the book.
I will put print statements in sections so that when you run the code it will tell you what section you are in.
Try to predict what is going on mentally.
< click on the number to create a break point where you can run the code until that point.
In the console there is a little step over button if you have one or multiple break points.
"""
import random

print("\tSection 1")

def maze2():
    response = input("You are lost in a maze. Will you go left or right? ")
    if response != "left":
        print("You fall in a pit. You lose.")
    else:
        maze2()


def guess_number_recursive():
    """Have the user guess a randomly generated number
    between 1 and 10
    inclusive."""
    # Generate the random number to be guessed.
    answer = random.randrange(10) + 1
    # INITIALIZE THE VARIABLE guess with a number entered by the user.
    guess = int(input("Guess a number between 1 and 10. "))
    try_it(answer, guess)

def try_it(answer, guess):
    """Determine if the current guess is the right
    answer."""
    # DEFINE A STOP CONDITION.
    if guess == answer:
        print("You guessed it!")
    elif answer > guess:
        guess = int(input("Guess higher! "))
        # HAVE THE FUNCTION CALL ITSELF.
        try_it(answer, guess)
    else:
        guess = int(input("Guess lower! "))
        # HAVE THE FUNCTION CALL ITSELF.
        try_it(answer, guess)

