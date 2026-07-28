"""
Program: W01 Tire Volume
Author: Michael Heiner

Description: The program calculates the approximate volume of a tire based on user-provided dimensions.
I have asked the user if they would like to buy the tires in the size the calculated and requested their phone number so they can be contacted with a quote. I added validation loops to prevent crashes if letters are typed instead of numbers. I also added loops to ensure valid "yes/no" answers, correct tire quantities, and valid 10-digit phone numbers before logging the data.
"""
# Use "import" function to get modules
import math
from datetime import datetime
# current date (Do NOT include time)
current_d_and_t = datetime.now()
# preset variables
num_tires = "N/A"
phone_number = "N/A"

# Have the user enter a tire width in mm.
tire_width = input("Enter the width of the tire in mm (ex 205): ")
while not tire_width.isdigit():
    tire_width=input("Im sorry I didn't understand that. Enter the width of the tire in mm (ex 205). Numbers only, please: ")
# Convert string to int
tire_width = int(tire_width)

# Have the user enter the aspect ratio.
aspect_ratio = input("Enter the aspect ratio of the tire (ex 60): ")
while not aspect_ratio.isdigit():
    aspect_ratio=input("Im sorry I didn't understand that. Enter the aspect ratio of the tire (ex 60). Numbers only, please: ")
# Convert string to int
aspect_ratio = int(aspect_ratio)

# Have the user enter the diameter of the wheel in inches.
diameter = input("Enter the diameter of the wheel in inches (ex 15): ")
while not diameter.isdigit():
    diameter=input("Im sorry I didn't understand that. Enter the diameter of the wheel in inches (ex 15). Numbers only, please: ")
# Convert string to int
diameter = int(diameter)

# Calculate and display the tire's volume.
volume = round((math.pi * tire_width ** 2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * diameter)) / 10000000000, 2)
print(f"The approximate volume is {volume:.2f} liters")

# Ask the user if they would like to buy tires in this size and start loop
buy_tires=input("Would you like to buy one or more tires in this size?(yes or no): ").lower()
#Check for Yes or No
while buy_tires not in ["yes", "no"]:
    buy_tires=input("I'm sorry I didn't understand that. Would you like to buy one or more tires in this size? Please type yes or no: ").lower()    
if buy_tires == "yes":
    # Ask the user how many tires they would like to buy
    num_tires=input("How many tires would you like to buy? 0, 1, 2, 3, or 4?: ")
        # Trap the user in a loop if a valid answer is not given. If they give any other answer give them a reminder.
    while num_tires not in ["0", "1", "2", "3", "4"]: 
        num_tires=input("I'm sorry I didn't understand that. How many tires would you like to buy? Please type 0, 1, 2, 3, or 4?: ")  
    
    # Received 0, 1, 2, 3, or 4 now ask for phone number   
    if num_tires != "0":
        phone_number=input("Please provide your phone number, with area code, so that we can call you with a quote. (Numbers only. Please, no (), -, ., or spaces): ")
        #Check that user phone number is 10 digit long
        while len(phone_number) !=10 or not phone_number.isdigit():
            phone_number=input("I'm sorry I didn't understand that. Please provide your phone number, with area code, so that we can call you with a quote. (NUMBERS ONLY, Please. no (), -, ., or spaces): ")
        
        #Thank the customer and let them know that we will be in touch
        print(f"Thank you! We will call you soon with a price quote. Have a great day!")
    
    # If number is a "0" 
    else: 
        print("Have a great day.")

# If "no" then print "Have a great day!"
else: 
    print("Have a great day.")
          
# Log the information in a text file.
with open("volumes.txt", mode="at") as volumes_file:
# current date (Do NOT include time), width of the tire, aspect ratio of the tire, diameter of the wheel, volume of the tire (rounded to two decimal places),(added)number of tires for purchase, and phone number
    print(f"{current_d_and_t:%Y-%m-%d}", tire_width, aspect_ratio, diameter, volume, num_tires, phone_number, sep=", ", file=volumes_file)