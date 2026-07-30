"""
Program: W05 Grocery Store
Author: Michael Heiner

Description:TBD

Exceeding the Requirements:TBD

Background
Your uncle has a grocery store, he has just started to use an online service that enables his customers to order groceries online. After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. Your uncle has asked you to write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.

User Requirements
The program must read two csv files, the customer's order and a product catalog. Each item in the customer's order will be looked up in the product catalog to get get the current price. An order will be displayed in the terminal that shows the customer's order details. Use the following details to create the program.

    1. Read the products inventory from the file products.csv.
    2. Read the customer's order from the file request.csv
    3. For each item in the order, look up the product in the catalog. Use the catalog information to calculate and display the order.
    4. Display the order receipt.
        4.1. Print a store name (you choose the name) at the top of the receipt.
        4.2. Print the list of ordered items. Include the item name, quantity ordered and price per item.
        4.3. Sum and print the number of ordered items.
        4.4. Sum and print the subtotal due.
        4.5. Compute and print the sales tax amount. Use 6% as the sales tax rate.
        4.6. Compute and print the total amount due.
        4.7. Print a thank you message.
        4.8. Get the current date and time from your computer’s operating system and print the current date and time.
        4.9. Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
"""
import csv

def main():
    """
    Reads the receipt.csv file, processes the file and displays the receipt according to the user requirements.
    """
    # product_dict Constants
    PRODUCT_NUM_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    #Call the read_dictionary func
    products_dict = read_dictionary("products.csv", 0)
    print(f"All products\n{products_dict}")
    print("Requested Items")

    # Open file safely
    with open("request.csv", "rt") as request_file:
        # 3. Create csv reader
        request_reader=csv.reader(request_file,delimiter=",")
        # 4. Skip header row
        next(request_reader)

        for row in request_reader:
            product_num = row[0]
            quantity = row[1]

            # Look up product info list in catalog
            info = products_dict[product_num]
            product_name = info[1]
            unit_price = info[2]

            
            print(f"{product_name}: {quantity} @ {unit_price}")

def read_dictionary(filename, key_column_index):
    """
    This function reads the product data from the csv file passed to the function in the filename parameter. The dictionary key is contained in the csv data column indicated by the key_column_index parameter, the value of each dictionary item is the list derived from the values in the row of the csv file. Function returns a dictionary of products.

    Parameters:
        filename: The path or name of the CSV file product information.
        key_column_index:The column index number used to extract the product information.

    Return Type:
        A dictionary where each key is a product # and each value is a list the product name and price.
    """
    # 1. Create empty dictionary
    products_dict={}

    # 2. Open file safely
    with open(filename,'rt') as csv_file:
        # 3. Create csv reader
        csv_reader=csv.reader(csv_file,delimiter=",")
        # 4. Skip header row
        next(csv_reader)

        # 5. Read row by row
        for row in csv_reader:
                # Extract key using the parameter
                key_value=row[key_column_index]
                # Store key-value pair
                products_dict[key_value]=row

    # 6. Return the products_dict
    return products_dict

# Call main to start this program.
if __name__ == "__main__":
    main()