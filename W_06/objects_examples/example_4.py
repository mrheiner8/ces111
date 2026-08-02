"""Object-Oriented Programming
Object-oriented programming is a programming paradigm based on the concept of objects. An object is a piece of a program that contains both data (also known as attributes) and functions (also known as methods).

When we write an object-oriented program, we combine data and functions together into objects. For example, if we were writing a registration program used by students to register for courses at a university, we would write code to create Student objects and Course objects. Each Student object would have data such as given_name, family_name, and phone_number and would have functions such as register, enroll, drop, and withdraw. Each Course object would have data such as course_code, title, description, and list_of_students and would have functions such as get_students and take_role.

Python includes many built-in and standard objects that a programmer can use to write programs. In fact, you have already used many objects in your programs. Python lists and dictionaries are objects and have attributes and methods. Readers and Writers from the csv module are also objects.

One of the marks of object-oriented programming is selecting attributes and calling methods using the dot operator (a period). The official name of the dot operator is component selector, but almost no one calls it that because the term “dot” is much easier to say than “component selector.” The code in example 4 uses the dot operator (.) to call the append method."""

# Example 4
def main():
    numbers = [87, 95, 72, 92, 95, 88, 84]
    numbers.append(78)
    numbers.append(72)
    print(numbers)
# Call main to start this program.
if __name__ == "__main__":
    main()

"""> python example_4.py
[87, 95, 72, 92, 95, 88, 84, 78, 72]

There are several types of commands that are commonly found in object-oriented programs. These types of commands are so common, that a programmer must be able to recognize and write them. Three of these types of commands are:

Creating objects, for example:
obj = datetime.now()

Accessing the attributes of an object using the dot operator (.), for example:
year = obj.year

Calling the methods of an object using the dot operator (.), for example:
new_obj = obj.replace(year=2035)
day_of_week = obj.weekday()"""
