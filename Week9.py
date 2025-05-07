"""
This is a summary of what we did in week 9. Examples from the thinking tasks as well as others from the book.
I will put print statements in sections so that when you run the code it will tell you what section you are in.
Try to predict what is going on mentally.
< click on the number to create a break point where you can run the code until that point.
In the console there is a little step over button if you have one or multiple break points.
"""
import random

print("\n\tSection 1: Working with numbers and input")
"""
When you take input, make sure you know that it is a string value, this pound_number will be a string so putting int()
around the input makes it an integer.
"""
overhead = 1.5
shipping = .86
per_pound = 15.5
pound_number = int(input("How many pounds of coffee would you like? \n"))
total = overhead + pound_number * per_pound + shipping * pound_number
print(f"You need to pay: ${total}")

print()

age = int(input("What is your age? \n"))
if age < 12:
    print("Your ticket costs $5")
elif age < 55:
    print("Your ticket costs $12")
else:
    print("Your ticket costs $8")

print()

answer = random.randrange(10) + 1
count = 0
guess = int(input("Guess a number between 1 and 10. "))
while guess != answer:
    if guess < answer:
        guess = int(input("Guess higher! "))
    else:
        guess = int(input("Guess lower! "))
    count += 1
print(f"You guessed it in {count} tries!")

for i in range(10,-1,-1):
    print(i)
print("Blast off!")

num_10 = 10
while num_10!=-1:
    print(num_10)
    num_10-=1
print("Blast off!")

user_num = int(input("What number would you like to count to? \n"))
while user_num != -1:
    print(user_num)
    user_num-=1
print("We counted to " + user_num + "!")

user_input = ""
while user_input != 'q' or user_input != 'Q':
    user_input = input("What would you like to do?\n"
                       "1- Enter your name\n"
                       "2- Enter your age\n"
                       "3- Enter your place of birth")

    if user_input == '1':
        name = input("What is your name? \n")
    elif user_input == '2':
        age = input("What is your age? \n")
    elif user_input == '3':
        birth = input("what is your place of birth? \n")
    else:
        print("That is not an option. ")

