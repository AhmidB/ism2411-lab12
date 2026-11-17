#1. Python is much faster when repeating the same steps every week because you just run the script once instead of clicking and filtering by hand. Excel is easier for quickly viewing data in a grid and making fast charts, while Python handles huge files and automatic cleanup without freezing.
#2.Tracking daily website orders or store sales totals would benefit from an append-mode log file. Append mode ("a") is the right tool because it adds each day's new total to the bottom of the file without erasing yesterday's history.
import csv
from datetime import datetime

# EXERCISE 2: Read and print raw rows
print("--- Exercise 2: Raw Rows ---")
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
print()

# EXERCISE 3: Skip the header
print("--- Exercise 3: Skip Header ---")
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)
print()

# EXERCISE 4: Compute totals
print("--- Exercise 4: Compute Totals ---")
overall_revenue = 0.0

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        overall_revenue = overall_revenue + total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Overall Total Revenue: ${overall_revenue:.2f}")
print()

# EXERCISE 5: Filter and write
print("--- Exercise 5: Filter and Write ---")
total_data_rows = 0
written_rows = 0

with open("data/sales.csv", "r") as infile:
    reader = csv.reader(infile)
    header = next(reader)
    
    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Product", "Price", "Qty", "Total"])
        
        for row in reader:
            total_data_rows = total_data_rows + 1
            product = row[0]
            price = float(row[1])
            qty = int(row[2])
            total = price * qty
            
            if total > 100:
                writer.writerow([product, price, qty, round(total, 2)])
                written_rows = written_rows + 1

print(f"Wrote {written_rows} qualifying rows out of {total_data_rows} original rows to data/cleaned.csv")
print()

# EXERCISE 6: csv.DictReader
print("--- Exercise 6: csv.DictReader ---")
dict_overall_revenue = 0.0

with open("data/sales.csv", "r") as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_overall_revenue = dict_overall_revenue + total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"DictReader Overall Total Revenue: ${dict_overall_revenue:.2f}")

# Comparison: csv.reader uses index numbers like row[0] which is good for simple files 
# without headers, while csv.DictReader uses column names like row["product"] which 
# is easier to read when a file has many columns.
print()

# EXERCISE 7: Sales summary by product
print("--- Exercise 7: Sales Summary by Product ---")
product_summary = {}

with open("data/sales.csv", "r") as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])
        product_summary[product] = product_summary.get(product, 0.0) + revenue

for product in sorted(product_summary):
    print(f"{product}: ${product_summary[product]:.2f}")
print()

# EXERCISE 8: Append mode log
print("--- Exercise 8: Append Mode Log ---")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log_file:
    log_file.write(f"{timestamp} | Total Revenue: ${overall_revenue:.2f}\n")

print(f"Logged run at {timestamp} to data/run_log.txt")