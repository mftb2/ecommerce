import csv
from datetime import datetime

# Function to read CSV file and return list of sales records
def read_sales_data(filename):
    sales_data = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['quantity'] = int(row['quantity'])
            row['price'] = float(row['price'])
            row['date'] = datetime.strptime(row['date'], '%Y-%m-%d')
            sales_data.append(row)
    return sales_data

# Function to calculate total sales
def calculate_total_sales(sales_data):
    total_sales = 0
    for record in sales_data:
        total_sales += record['quantity'] * record['price']
    return total_sales

# Function to calculate sales per product
def calculate_sales_per_product(sales_data):
    sales_per_product = {}
    for record in sales_data:
        product = record['product']
        sales_amount = record['quantity'] * record['price']
        if product not in sales_per_product:
            sales_per_product[product] = 0
        sales_per_product[product] += sales_amount
    return sales_per_product

# Function to find the best-selling product
def find_best_selling_product(sales_data):
    sales_per_product = calculate_sales_per_product(sales_data)
    best_selling_product = max(sales_per_product, key=sales_per_product.get)
    return best_selling_product, sales_per_product[best_selling_product]

# Function to find total quantity sold
def calculate_total_quantity(sales_data):
    total_quantity = 0
    for record in sales_data:
        total_quantity += record['quantity']
    return total_quantity

# Main function to perform sales analysis
def main():
    filename = 'sales_data.csv'
    sales_data = read_sales_data(filename)
    
    total_sales = calculate_total_sales(sales_data)
    sales_per_product = calculate_sales_per_product(sales_data)
    best_selling_product, best_selling_amount = find_best_selling_product(sales_data)
    total_quantity = calculate_total_quantity(sales_data)

    print(f"Total Sales: ${total_sales:.2f}")
    print("Sales Per Product:")
    for product, sales in sales_per_product.items():
        print(f"  {product}: ${sales:.2f}")
    print(f"Best-Selling Product: {best_selling_product} (${best_selling_amount:.2f})")
    print(f"Total Quantity Sold: {total_quantity}")

if __name__ == '__main__':
    main()
