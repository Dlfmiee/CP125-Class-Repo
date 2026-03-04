# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv

def summarize_sales(input_file, output_file):
    revenues = []
    
    # Open sales CSV
    f = open(input_file, "r", newline="")
    reader = csv.reader(f)
    next(reader)
    
    for line in reader:
        product = line[0]
        quantity = int(line[1])
        price = float(line[2])
        
        revenue = quantity * price
        revenues.append(revenue)
    
    f.close()
    
    total = sum(revenues)
    average = total / len(revenues)
    highest = max(revenues)
    lowest = min(revenues)
    
    out = open(output_file, "w")
    
    out.write(f"Total Revenue: ${total:.2f}\n")
    out.write(f"Average Revenue: ${average:.2f}\n")
    out.write(f"Highest Revenue: ${highest:.2f}\n")
    out.write(f"Lowest Revenue: ${lowest:.2f}\n")
    
    out.close()
    
    return (total, average, highest, lowest)

# Test your code here
result = summarize_sales("labs/lab08/exercise5/data/sales.csv", "labs/lab08/exercise5/data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
