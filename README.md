# midterm_project
Dosa Restaurant Order Processing Project
Project Overview:
This project processes JSON data representing customer orders at a Dosa restaurant. It extracts customer contact information and item details from the orders and saves the results into two distinct JSON files:

customers.json: This file maps customer phone numbers to their respective names.
items.json: This file keeps track of the items ordered, including the price and the total number of times each item has been purchased.
The goal of this project is to create an efficient system for analyzing and managing customer and item data using Python's built-in libraries and data structures.

Design Overview:
Input:

A JSON file containing a list of orders. Each order has details like customer name, phone number, and the items purchased (with attributes such as item name, price, and quantity).
Output:

customers.json: A JSON file where each key is a customer’s phone number, and the corresponding value is the customer’s name.
items.json: A JSON file where each key is the name of an item, and the value is a nested dictionary containing:
The item's price
The total number of times the item has been ordered.
Requirements:
Python 3.x installed on your system.
Steps to Use:
Place the Input File: Ensure the JSON file (e.g., example_orders.json) is located in the same directory as the script. The file should be formatted correctly, containing the necessary customer order details.

Run the Script: Execute the Python script using the following command:

bash
Copy code
python3 midproject.py example_orders.json
Check the Output: After running the script, you will see two JSON files generated in the project directory:

customers.json: A JSON file containing a mapping of phone numbers to customer names.
items.json: A JSON file with item names as keys, and each key holds a dictionary with the item's price and the total number of orders that included that item.
