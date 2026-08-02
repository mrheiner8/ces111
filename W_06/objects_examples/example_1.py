"""W06 Learning Activity: Objects
A paradigm is a way of thinking or a way of perceiving the world. There are at least four main paradigms for programming a computer: procedural, declarative, functional, and object-oriented. During most of CSE 110 and 111, you used procedural programming. During this week, you will be introduced to object-oriented programming.

Programming Paradigms
Procedural Programming
Procedural programming is a way of programming that focuses on the process or the steps to accomplish a task. For example, if we had 100 numbers and wanted to know the average value of those 100 numbers, we could add the numbers and then divide by 100. This is one process to compute the average of numbers: add them and divide by the quantity of numbers. A Python procedural program for computing the average is shown in example 1."""

# Example 1
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    total = 0
    for x in numbers:
        total += x
    average = total / len(numbers)
    print(f"average: {average:.2f}")
# Call main to start this program.
if __name__ == "__main__":
    main()

"""
> python example_1.py
average: 87.57
Notice that with procedural programming, we must write the process or the steps that are necessary to complete a task. Procedural programming is the type of programming that you did most often in CSE 110 and 111."""