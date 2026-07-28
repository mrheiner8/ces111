"""
IndexError
Recall from week 4 that each element in a list is stored at a unique index and that an index is always an integer. If we write code that tries to use an index that doesn’t exist in a list, when the computer executes that code, the computer will raise an IndexError.

The program in example 6 is similar to example 5, and both programs cause the computer to raise an IndexError. The program in example 6 creates a list that contains three surnames. Then the program attempts to print the surname at index 3. Of course, this statement fails because the list contains only three elements, and the index of the last element is 2.
"""
# Example 6
def main():
  try:
    # Create a list that contains three family names.
    surnames = ["Smith", "Lopez", "Marsh"]
    # Attempt to print the surname at index 3. Because
    # there are only three names in the surnames list and
    # therefore the last index is 2, this statement will
    # fail and cause the computer to raise an IndexError.
    print(surnames[3])
  except IndexError as index_err:
    print(index_err)
if __name__ == "__main__":
  main()
"""  
> python index_error_read.py
list index out of range
"""