"""Functional Programming
When we use functional programming to program a computer, we focus on the functions necessary to accomplish a task. Mathematicians often find functional programming natural for them because they are accustomed to using functions while studying mathematics. In functional programming, functions are so important that we often pass functions into other functions.
"""
# Example 3
from functools import reduce
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    func_add = lambda a, b: a + b
    total = reduce(func_add, numbers)
    average =  total / len(numbers)
    print(f"average: {average:.2f}")
# Call main to start this program.
if __name__ == "__main__":
    main()
"""
> python example_3.py
average: 87.57

Notice how example 3 uses three functions: a lambda function, the reduce function, and the len function. Notice also that the lambda function is passed into the reduce function. Passing a function into a function is one of the marks of functional programming."""