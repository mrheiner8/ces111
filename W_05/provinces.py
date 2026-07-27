"""I wrote this with function instead of in line code for practice"""
def main():
    # Read the contents of a text file named provinces.txt into a list.
    text_list = read_list("provinces.txt")

    # Print the entire list.
    print(text_list)

    # New list with book ends removed.
    text_list = remove_bookends(text_list)

    # Print the new list with book ends removed.
    #print(f'Full list with book ends removed:{text_list}')

    # New list where 'AB' is replaced with 'Alberta'.
    text_list = modified_alberta(text_list)
    
    # Print the new list where 'AB' is replaced with 'Alberta'.
    #print(f'Full list where "AB" is replaced with "Alberta":{text_list}')

    # Number of times 'Alberta' is found in 'text_list'.
    count = alberta_count(text_list)
    
    # Print the number of times 'Alberta' is found in 'text_list'.
    print(f'Alberta occurs {count} times in the modified list.')

def read_list(filename):
    """Read the contents of a text file into a list and return the list. Each element in the list will contain one line of text from the text file. 
    
    Parameter filename: 
        the name of the text file to read 
    Return: 
        a list of strings
    """
    # Create an empty list that will store the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:     

        # Read the contents of the text file one line at a time.
        for line in text_file:     

            # Remove white space, if there is any, from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text onto the end of the list.
            text_list.append(clean_line)

        # Return the list that contains the lines of text.
    return text_list   
     # Call main to start this program.

def remove_bookends(text_list):
    """Read the contents of text_list into a list and return the list with the "bookends" removed. Each element in the list will contain one line of text from the text file. 
    
    Parameter text list: 
        a list of strings
        
    Return: 
        a list of strings
    """
    # Create a list that will store the lines of text from the text file with the "bookends" removed.
    # Remove the first item (at index 0)
    text_list.pop(0)

    # Remove the last item (default when no index is given)
    text_list.pop()

    return text_list

def modified_alberta(text_list):
    """Read the contents of text_list into a list and return the list where 'AB' is replaced with 'Alberta'. Each element in the list will contain one line of text from the text file. 
    
    Parameter text list: 
        a list of strings 
        
    Return: 
        a list of strings
    """
    # Create a list that will store the lines of text from the text file where 'AB' is replaced with 'Alberta'.
    # Loop over each position index
    for i in range(len(text_list)):
        if text_list[i] == "AB":
            # replace "AB" with full word "Alberta"
            text_list[i] = "Alberta"

    return text_list

def alberta_count(text_list):
    """Read the contents of text_list. Count the number of elements that are "Alberta" and print that number.

    Parameter text list: 
        a list of strings 
        
    Return: 
        an int
    """
    # Create a list that will store the lines of text from the text file where 'AB' is replaced with 'Alberta'.
    count = text_list.count("Alberta")

    return count

if __name__ == "__main__":
    main()