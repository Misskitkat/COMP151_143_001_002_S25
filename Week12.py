"""
This is a summary of what we did in week 12. Examples from the thinking tasks as well as others from the book.
I will put print statements in sections so that when you run the code it will tell you what section you are in.
Try to predict what is going on mentally.
< click on the number to create a break point where you can run the code until that point.
In the console there is a little step over button if you have one or multiple break points.
"""

class GroceryStore:
    """A simple attempt to model a grocery store."""
    def __init__(self, name, location):
        """Initialize name and location attributes."""
        self.name = name
        self.location = location
    def open(self):
        """Simulate a store opening at the beginning of the day."""
        print(f"{self.name} is now open.")
    def close(self):
        """Simulate a store closing at the end of the day."""
        print(f"{self.name} is now closed.")

store_near_campus = GroceryStore('Market Basket', 'Bridgewater')
print(f"A store near campus is {store_near_campus.name}.")
print(f"The store is located in {store_near_campus.location}.")

store_near_campus.open()
print("Let's buy some groceries at the store near campus.")
store_near_campus.close()

store_near_dr_g = GroceryStore("Johnny's Food Master", "Somerville")
store_on_commute = GroceryStore("Market Basket", "West Bridgewater")