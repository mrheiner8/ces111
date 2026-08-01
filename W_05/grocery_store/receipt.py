# receipt.py
"""
Program: W05 Grocery Store
Author: Michael Heiner

Description:
    The program must read two csv files, the customer's order and a product catalog. Each item in the customer's order will be looked up in the product catalog to get get the current price. An order will be displayed in the terminal that shows the customer's order details.

Exceeding the Requirements:
    Find the last time on the shopping list and offer the customer a coupon for that item on their next purchase of that item.
"""
import csv
from datetime import datetime
def main():
    """
    Reads the receipt.csv file, processes the file and displays the receipt according to the user requirements.
    """
    # product_dict Constants
    PRODUCT_NUM_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    try:
        #Call the read_dictionary func
        products_dict = read_dictionary("products.csv", 0)
        print("Colorado Springs Grocery Store")

        # Open file safely
        with open("request.csv", "rt") as request_file:
            # Create csv reader
            request_reader=csv.reader(request_file,delimiter=",")
            # Skip header row
            next(request_reader)

            # Initialize accumulators BEFORE the loop
            total_items = 0
            subtotal = 0

            # Coupon calculation variables 
            max_item_cost = 0.0
            coupon_product = ""

            # Process each item inside the loop
            for row in request_reader:
                product_num = row[0]
                quantity = int(row[1])

                # Look up product info list in catalog
                info = products_dict[product_num]
                product_name = info[NAME_INDEX]
                unit_price = float(info[PRICE_INDEX])

                # Accumulate running totals
                total_items += quantity

                # Math for sub total
                subtotal += (quantity * unit_price)

                # find the last item on the shopping list
                coupon_product = product_name

                # Print line items only
                print(f"{product_name}: {quantity} @ ${unit_price}")

        # Math for sales tax and total cost
        sales_tax = (subtotal * .06)
        total_cost = (subtotal + sales_tax)

        # Get date and time
        current_date_and_time = datetime.now()

        # print the rest of the receipt 
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total:  ${total_cost:.2f}")
        print("Thank you for shopping Colorado Springs Grocery Store!")
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")     
        # Print coupon
        print(f"\n!!!Special Coupon!!!\nSave 10% on your next purchase of {coupon_product}!")

    except FileNotFoundError as file_err:
        print("Error: missing file")
        print(file_err)

    except PermissionError as perm_err:
        print("Error: permission denied")
        print(perm_err)

    except KeyError as key_err:
        print("Error: unknown product ID in the request file")
        print(key_err)
     

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
# End receipt.py