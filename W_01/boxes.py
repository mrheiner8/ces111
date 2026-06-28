"""
Program: W01
Author: Michael Heiner

Description:Activity: Calling Functions
Purpose
Check your understanding of calling built-in Python functions and functions that are in a standard Python module.

Problem Statement
In our modern world economy, many items are manufactured in large factories, then packed in boxes and shipped to distribution centers and retail stores. A common question for employees who pack items is “How many boxes do we need?”

Assignment
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers:

the number of manufactured items
the number of items that the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.

Helpful Documentation
The math.ceil() function rounds a number up to the nearest integer that is greater than or equal to a number.
Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Run your program and enter the inputs shown below. Ensure that your program’s output matches the output below.
> python boxes.py
Enter the number of items: 8
Enter the number of items per box: 5
For 8 items, packing 5 items in each box, you will need 2 boxes.
> python boxes.py
Enter the number of items: 25
Enter the number of items per box: 4
For 25 items, packing 4 items in each box, you will need 7 boxes.
"""
import math

items=int(input("Enter the number of items: "))
items_per_box=int(input("Enter the number of items per box: "))

print(f"For {items} items, packing {items_per_box} items in each box, you will need {math.ceil(items / items_per_box)} boxes.")

# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""
A manufacturing company needs a program that will help its employees
pack manufactured items into boxes for shipping. Write a Python
program named boxes.py that asks the user for two integers:  1) the
number of manufactured items and 2) the number of items that the user
will pack per box. Your program must compute and print the number of
boxes necessary to hold the items. This must be a whole number. Note
that the last box may be packed with fewer items than the other boxes.


# Import the math module so that we can call the math.ceil function.
import math

# Get two numbers from the user.
num_items = int(input(f"Enter the number of items: "))
items_per_box = int(input(f"Enter the number of items per box: "))

# Compute the number of boxes by dividing
# and then calling the math.ceil function.
num_boxes = math.ceil(num_items / items_per_box)

# Display a blank line.
print()

# Display the results for the user to see.
print(f"For {num_items} items, packing {items_per_box}"
    f" items in each box, you will need {num_boxes} boxes.")
"""