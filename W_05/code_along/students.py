"""
Program:
This program will read data from a comma separated file (csv) of student information into a dictionary. This dictionary will then be used to lookup student information by ID number.

Requirements:
Your program must do the following:

    1. Open the students.csv file for reading, skip the first line of text in the file because it contains only headings, and read the other lines of the file into a dictionary. The program must store each student ID Number as a key and each ID Number name pair or each name as a value in the dictionary.

    2. Get an ID Number from the user, use the ID Number to find the corresponding student name in the dictionary, and print the name.

    3. If a user enters an ID Number that doesn’t exist in the dictionary, your program must print the message, "No such student" (without the quotes).
"""
import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a scv file into a compound dictionary and return the dictionary.
        
    Parameters
        filename:
            The name of a CSV file to read.
        Key_column_index:
            The index of the column to use as the keys in the dictionary.
        
    return:
        A compound dictionary that contains the content of the CSV file.
        """
    s_dictionary={}
    with open(filename,'rt') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=",")
        next(csvreader)
        for row in csvreader:
                key_value=row[key_column_index]
                s_dictionary[key_value]=row
    return s_dictionary



def main():
    KEY_INDEX=0
    NAME_INDEX=1
    students=read_dictionary('students.csv',KEY_INDEX)
    i_number=input("\nPlease enter an I-number: ")
    i_number=i_number.replace("-","")

    if not i_number.isdigit():
         print("\nInvalid ID Number\n")
    elif len(i_number) !=9:
        print("An I-Number must be 9 digits long")
    else:
        if i_number in students:
            
            student=students[i_number]
            name=student[NAME_INDEX]
            print(f"\nThe students name is {name}.\n")
        else:
            print("\nNo such student!\n")

# Call main to start this program.
if __name__ == "__main__":
    main()



"""
Enhancements
Here is a list of enhancements that you could make to the program. Your instructor will walk you through at least one of them. Feel free to complete others.

    1. Add code to remove dashes from the ID Number that the user enters. This will allow the user to enter ID Numbers with dashes or without dashes and still allow the computer to search in the dictionary.

    2. When a user enters an ID Number, your program should ensure it is a valid ID Number.

        2.1. If there are too few digits in the ID Number, your program should print, "Invalid ID Number: too few digits" (without the quotes).

        2.2. If there are too many digits in the ID Number, your program should print, "Invalid ID Number: too many digits" (without the quotes).

        2.3. If the given ID Number contains any characters besides digits and dashes, your program should output "Invalid ID Number" (without the quotes).

    3. Add something or change something in your program that you think would make your program better, easier for the user, more elegant, or more fun. Be creative.
"""