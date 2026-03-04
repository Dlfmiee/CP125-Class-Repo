# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:

import csv

def calculate_order_total(products_file, order_file, output_file):
    products = {}
    
    # Read products file
    f = open(products_file, "r", newline="")
    reader = csv.reader(f)
    next(reader)
    
    for line in reader:
        product_id = line[0]          # ✅ use product_id
        price = float(line[2])
        products[product_id] = price
    
    f.close()
    
    total = 0.0
    
    # Read order file
    z = open(order_file, "r", newline="")
    reader = csv.reader(z)
    next(reader)
    
    # Open output file
    out = open(output_file, "w", newline="")
    writer = csv.writer(out)
    
    writer.writerow(["product_id", "total_cost"])
    
    for line in reader:
        product_id = line[0]
        quantity = int(line[1])
        
        if product_id in products:
            item_total = products[product_id] * quantity
            total += item_total
            
            writer.writerow([product_id, f"{item_total:.2f}"])
    
    z.close()
    out.close()
    
    return total


# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
