
# Dosa Restaurant Order Processing Project


## Project Overview

This project reads JSON data from a file (e.g., a file containing orders), processes the data to extract customer information and item details, and then writes the results to two separate JSON files:

- **customers.json**: Contains a mapping of customer phone numbers to their names.
- **items.json**: Contains a list of items ordered, their price, and the total number of times each item has been ordered.

This program is designed to be efficient, using Python's built-in libraries and data structures to manage and process the data effectively.

## Design

### Input:
A JSON file containing an array of orders. Each order includes customer information (name and phone number) and items ordered (name and price).

### Output:
1. **customers.json**: A JSON file mapping customer phone numbers to their corresponding names.
2. **items.json**: A JSON file containing the item names, prices, and the number of times each item was ordered.

## Prerequisites:
- Ensure that Python 3.x is installed on your machine.

## Instructions:

1. **Prepare the Input File:**
   Place the JSON file containing the orders (e.g., `example_orders.json`) in the project directory. Ensure that the file follows the correct structure for processing.

2. **Execute the Python Script:**
   Run the script with the following command:
   `python3 middosa.py example_orders.json`

3. **View the Output:**
After execution, two output files will be generated in the project directory:

- `customers.json`: Contains the customer names and phone numbers.
- `items.json`: Contains the item details, including the price and number of times each item has been ordered.



