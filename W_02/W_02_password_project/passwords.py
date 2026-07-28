"""
Program: W01 Password Strength

Author: Michael Heiner

Description: This program evaluates the strength of a user-provided password on a scale of 0 to 5 by checking it against common dictionary words, evaluating its length, and calculating a complexity score based on character types. 

Additionally, a robust confirmation loop was implemented to improve the user experience. This feature verifies the input before scoring it and includes precise exit conditions, allowing the user to gracefully quit the program at any point during the prompts by typing 'Q' without getting trapped in the loop or accidentally scoring the quit command.
"""

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def main():
    """Provides the user input loop. The loop asks the user for a password to test. If that password is anything but "q" or "Q" call the password_strength function and report the results to the user. If the user enters "q" or "Q", quit the program."""
    
    user_pw = input('Welcome to the password checker.\nTo get the best score your password must be at least 10 characters long \nand contain at least one uppercase letter, one lowercase letter, one number, and one special character.\nPlease type your password now. \nOr, to quit the password checker type the letter "Q": ')
   
    # check for “user_pw not in [“Q” or “q”] “> Enter the loop
    while user_pw not in ["q", "Q"]:
    
        # Confirm user_pw by trapping them in a confirmation loop
        pw_confirm = input (f'\nYou typed "{user_pw}". \nIs that correct? (yes or no)?\nTo quit the password checker type the letter "Q": ')
        if pw_confirm in ["q", "Q"]:
            user_pw = pw_confirm
            break 
       
        # If “yes” exit confirmation loop 
        # If “no” ask “user_pw = input("Please type your password. To quit the password checker type the letter 'Q': ")
        while pw_confirm.lower() != "yes": 
            user_pw = input('\nPlease type your password now. \nTo quit the password checker type the letter "Q": ')
            if user_pw in ["q", "Q"]:
                break
            pw_confirm = input (f'\nYou typed "{user_pw}". \nIs that correct? (yes or no)?\nTo quit the password checker type the letter "Q": ')
            if pw_confirm in ["q", "Q"]:
                user_pw = pw_confirm
                break

        if user_pw in ["q", "Q"]:
                break
        # Call the function and save the returned score
        score = password_strength(user_pw)
        
        # If user receives a score of 2, 3, or 4 recommend adding in some complexity to strengthen there password.
        print(f'\nYour password "{user_pw}" has received a score of {score} out of 5.')
        if score in [2, 3, 4]:
            print(f'Try to increase your score by making sure you password contains at least one uppercase letter, one lowercase letter, one number, and one special character.' )
        
        # Use the 'score' variable in your prompt for the next loop
        if score == 5:
            print("This is a good password!")
        
        # If another password is entered re-enter the loop    
        user_pw = input('\nIf you would like to try another password please enter it now. \nTo quit the password checker type the letter "Q": ')
        #If “Q” exit loop” 
    
    if user_pw in ["q", "Q"]:
        print('\nHave a great day!')

def word_in_file (word, filename, case_sensitive=False):
    """This function reads a file (specified by the filename parameter) in which each line of the file contains a single word. If the word passed in the word parameter matches a word in the file the function returns a true otherwise it returns a false. If the parameter case_sensitive is true a case sensitive match is performed. If case_sensitive is false a case insensitive match is performed. The case_sensitive parameter should default to False"""
    with open(filename, "r",encoding="utf-8") as f:
        # Convert word to lower case
        if case_sensitive == False:
            word = word.lower()
        # Read through the file line by line
        for line in f:
            clean_line = line.strip()
            if case_sensitive == False:
            # Strips off leading and trailing whitespace
                clean_line = clean_line.lower()
            if word == clean_line:
                return True    
    return False
    	

def word_has_character (word, character_list):
    """This function loops through each character in the string passed in the word parameter to see if that character is in the list of characters passed in the character_list parameter. If any of the characters in the word are present in the character list return a true, If none of the characters in the word are in the character list return false"""
    for letter in word:
        if letter in character_list:
            return True
    return False
    	

def word_complexity (word):
    """This function creates a numeric complexity value based on the types of characters the word parameter contains. One point of complexity is given for each type of character in the word. The function calls the word_has_character function for each of the 4 kinds of characters (LOWER, UPPER, DIGITS, SPECIAL). If the word has that kind of character a point is added to complexity rating. Since there are 4 kinds of characters the complexity rating will range from 0 to 4. (0 would be returned only if word contained no characters or only contains characters that are not in any of the lists.)"""
    complexity_score = 0
    if word_has_character(word, LOWER):
        complexity_score += 1
    if word_has_character(word, UPPER):
        complexity_score += 1
    if word_has_character(word, DIGITS):
        complexity_score += 1
    if word_has_character(word, SPECIAL):
        complexity_score += 1    
    return complexity_score
    	
   
def password_strength (password, min_length = 10, strong_length = 16):
    """This function checks length requirements, checks dictionary and known-passwords, calls word_complexity to calculate the word's complexity then determines the password's strength based on the user requirements. It should print the messages defined in the requirements and return the password's strength as a number from 0 to 5. The min_length parameter should have a default value of 10. The strong_length parameter should have a default value of 16"""
    
    if word_in_file(password, "wordlist.txt")== True:
        print('\nPassword is a dictionary word and is not secure.')
        return 0
    if word_in_file(password, "toppasswords.txt", True)== True:
        print('\nPassword is a commonly used password and is not secure.')
        return 0
    if len(password) < min_length:
        print('\nPassword is too short and is not secure.')
        return 1
    if len(password) >= strong_length: 
        print ('\nPassword is long, length trumps complexity this is a good password.')
        return 5
    else:
        return word_complexity(password) + 1

if __name__ == "__main__":
    main()