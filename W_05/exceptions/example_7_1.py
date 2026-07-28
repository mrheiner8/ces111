"""
KeyError
As shown in example 7, if we write code that attempts to find a key in a dictionary and that key doesn`t exist in the dictionary, then the computer will raise a KeyError.

See Example 7

Of course, it is very unlikely that a programmer would write a program that tries to find a hard-coded key that is not in a dictionary. However, it is common for a user to enter a key that is not in a dictionary. This is why the programs in examples 1 and 4 in the prepare content for lesson 8 include an if statement above the line of code that searches the dictionary, like this:
"""
# Example 7.1
# Get a student ID from the user.
id = input("Enter a student ID: ")
# Check if the student ID is in the dictionary.
if id in students:
  # Find the student ID in the dictionary and
  # retrieve the corresponding student name.
  name = students[id]
  # Print the student's name.
  print(name)
else:
  print("No such student")