"""TypeError
The computer raises a TypeError when the code that calls a function passes an argument with the wrong data type. The code in example 2 attempts to pass a string to the round function. This causes the computer to raise a TypeError because the round function cannot round a string to an integer. It can round only a number to an integer. The output below example 2 shows that the computer raised a TypeError."""

# Example 2
def main():
  try:
    text = input("Please enter a number: ")
    integer = round(text)
    print(integer)
  except TypeError as type_err:
    print(type_err)
if __name__ == "__main__":
  main()

"""> python type_error.py
Please enter a number: 25.7
type str doesn't define __round__ method"""