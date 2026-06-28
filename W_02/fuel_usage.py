def main():
  # Get an odometer value in U.S. miles from the user.
    start_miles = input("Enter the first odometer reading (miles): ")
    """while not start_miles.isfloat():
        start_miles=input("Im sorry I didn't understand that. Enter the first odometer reading in miles (ex 30462). Numbers only, please: ")
        
        Spot on with float()! That is exactly the function you need to handle decimal numbers.
        However, there is a small snag: .isfloat() is not actually a built-in command in Python, so your code will throw an error if you try to run it. Checking if a string is a float usually requires a slightly more advanced technique in Python (like using a try...except block).
        To keep you moving forward and focused on the core assignment, I recommend removing the while loops for now. You can just wrap the input directly like this: float(input("...")). We can always add validation back in later if you want a challenge!"""
    # Convert string to float
    start_miles = float(start_miles)
  # Get another odometer value in U.S. miles from the user.
    end_miles = input("Enter the second odometer reading (miles): ")
    """while not end_miles.isfloat():
        end_miles=input("Im sorry I didn't understand that. Enter the second odometer reading in miles (ex 30810). Numbers only, please: ")"""
# Convert string to float
    end_miles = float(end_miles)
  # Get a fuel amount in U.S. gallons from the user.
    amount_gallons = input("Enter the amount of fuel used (gallons): ")
    """while not amount_gallons.isfloat():
        amount_gallons=input("Im sorry I didn't understand that. Enter the amount of fuel used in gallons (ex 11.2). Numbers only, please: ")"""
# Convert string to float
    amount_gallons = float(amount_gallons)
  # Call the miles_per_gallon function and store
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
  # the result in a variable named mpg.
  # Call the lp100k_from_mpg function to convert the
    lp100k = lp100k_from_mpg(mpg)
  # miles per gallon to liters per 100 kilometers and
  # store the result in a variable named lp100k.
  # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon\n{lp100k:.2f} liters per 100 kilometers")
  
def miles_per_gallon(start_miles, end_miles, amount_gallons):
  """Compute and return the average number of miles
  that a vehicle traveled per gallon of fuel.
  Parameters
  start_miles: An odometer value in miles.
  end_miles: Another odometer value in miles.
  amount_gallons: A fuel amount in U.S. gallons.
  Return: Fuel efficiency in miles per gallon.
  """
  miles_per_gallon = (end_miles - start_miles) / amount_gallons
  return miles_per_gallon

def lp100k_from_mpg(mpg):
  """Convert miles per gallon to liters per 100
  kilometers and return the converted value.
  Parameter mpg: A value in miles per gallon
  Return: The converted value in liters per 100km.
  """
  lp100k_from_mpg = 235.215 / mpg
  return lp100k_from_mpg
# Call the main function so that
# this program will start executing.
main()

"""Sample Solution
The following shows one way to solve this problem. It is not the only way this problem can be solved.

check-1_solution.py

# Copyright 2020, Brigham Young University-Idaho. All rights reserved.


Write a Python program named fuel_usage.py that asks the user
for three numbers:
1. A starting odometer value in miles
2. An ending odometer value in miles
3. A amount of fuel in gallons

Your program must calculate and print fuel efficiency in both
miles per gallon and liters per 100 kilometers. Your program
must have three functions named as follows:
1. main
2. miles_per_gallon
3. lp100k_from_mpg

All user input and printing must be in the main function. In other
words, the miles_per_gallon and lp100k_from_mpg functions must not
call the the input or print functions.


def main():
    # Get an odometer value in U.S. miles from the user.
    start_miles = float(input(
            "Enter the first odometer reading (miles): "))

    # Get another odometer value in U.S. miles from the user.
    end_miles = float(input(
            "Enter the second odometer reading (miles): "))

    # Get a fuel amount in U.S. gallons from the user.
    amount_gallons = float(input(
            "Enter the amount of fuel used (gallons): "))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Display the results for the user to see.
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    ""Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    ""
    mpg = abs(end_miles - start_miles) / amount_gallons
    return mpg


def lp100k_from_mpg(mpg):
    ""Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    ""
    lp100k = 235.215 / mpg
    return lp100k


# Call the main function so that
# this program will start executing.
main()


A few questions about this part.
1. What does abs mean?
2. They used “mpg” in the calculation of the function with “return = mpg” , I used “miles_per_gallon”in the calculation of my function with “return= miles_per_gallon” our call in the main function looks the same. Does “return= (variable_name)” not create that name for main to use? 
3. Why do both functions seem to work the same?  

These are excellent questions that hit on some of the most important concepts in programming: variable scope and data flow!
Here is the breakdown of exactly what is happening in both examples:

1. What does abs mean?
abs() is a built-in Python function that stands for absolute value. It turns any negative number into a positive number (and leaves positive numbers alone).
In the sample solution, it is used as a safety net. If a user accidentally types the ending odometer reading first and the starting odometer reading second, subtracting them would normally result in a negative number (e.g., 30462 - 30810 = -348). You cannot drive negative miles, so wrapping the math in abs() forces the distance to be positive 348 no matter what order the user typed the numbers.

2. Does return = (variable_name) create that name for main to use?
No, it does not. This is a very common misconception!
When you use the return statement, Python only passes back the raw data (the actual calculated number), not the variable's name.
Think of a function like a locked room. Any variable you create inside that room (whether you name it miles_per_gallon, mpg, x, or pineapple) is trapped inside. This is called local scope. When the function finishes its job, it takes the number stored in that variable, slides it under the door to main(), and then the room (along with its internal variable names) disappears.

3. Why do both functions seem to work the same?
They work the same because main() does not care what the helper function called its variables internally. main() is only waiting to catch the raw number that gets slid under the door.
Look at your call in main():
mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
This line is telling Python:

1. "Go run the miles_per_gallon function."

2. "Whatever raw number it spits out at the very end, grab it."

3. "Create a brand new variable inside main called mpg, and put that number inside it."

Because main() is the one assigning the final number to its own mpg variable, it does not matter if the helper function used miles_per_gallon = ... or mpg = ... to do the math. As long as both functions calculate the correct math and return the correct number, the final result will be exactly the same."""