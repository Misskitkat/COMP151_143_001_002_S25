"""
This is a summary of what we did in week 10. Examples from the thinking tasks as well as others from the book.
I will put print statements in sections so that when you run the code it will tell you what section you are in.
Try to predict what is going on mentally.
< click on the number to create a break point where you can run the code until that point.
In the console there is a little step over button if you have one or multiple break points.
"""
print("\tSection 1")

"""
When you take input, make sure you know that it is a string value, this pound_number will be a string so putting int()
around the input makes it an integer. This first one is printing inside so you do not need to create a return
"""
def coffee_order():
    overhead = 1.5
    shipping = .86
    per_pound = 15.5
    pound_number = int(input("How many pounds of coffee would you like? \n"))
    total = overhead + pound_number * per_pound + shipping * pound_number
    print(f"You need to pay: ${total}")

coffee_order()

def favorite_book(book_title):
    print(f'One of my favorite books is: {book_title.title()}')

favorite_book("harry potter and the philosophers stone")

def parts_of_speech(noun, adverb, adjective):
    print(f'{noun} is {adverb} {adjective}')

parts_of_speech("Dr. Gross", "really", "helpful")

