
# ISM2411 Lab 12
# Name: Bernard Bezerra

# REFLECTION 1:
# This ETL process is similar to using Excel to filter data and
# calculate totals. Python makes it easier to automate repeated
# tasks and process large datasets, while Excel is easier for
# quick visual analysis, charts, and manual changes.

# REFLECTION 2:
# A business could use append mode to record daily sales revenue.
# Append mode is useful because it preserves previous records
# and adds new entries without deleting the existing history.

import csv
from datetime import datetime

# EXERCISE 1
file_path = "data/sales.csv"

# EXERCISE 2
print("\nEXERCISE 2")
with open(file_path, "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# EXERCISE 3
print("\nEXERCISE 3")
with open(file_path, "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# EXERCISE 4
print("\nEXERCISE 4")
total_revenue = 0

with open(file_path, "r", newline="") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        product, price, quantity = row
        price = float(price)
        quantity = int(quantity)
        revenue = price * quantity
        total_revenue += revenue

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

# EXERCISE 5
print("\nEXERCISE 5")
original_count = 0
cleaned_count = 0

with open(file_path, "r", newline="") as source:
    reader = csv.reader(source)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            product, price, quantity = row
            price = float(price)
            quantity = int(quantity)
            total = price * quantity
            original_count += 1

            if total > 100:
                writer.writerow([
                    product,
                    f"{price:.2f}",
                    quantity,
                    f"{total:.2f}"
                ])
                cleaned_count += 1

print(f"Original rows: {original_count}")
print(f"Cleaned rows: {cleaned_count}")

# EXERCISE 6
print("\nEXERCISE 6")


dict_total = 0

with open(file_path, "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        revenue = price * quantity
        dict_total += revenue
        print(f"{product}: ${revenue:.2f}")

print(f"DictReader total: ${dict_total:.2f}")

# EXERCISE 7
print("\nEXERCISE 7")
sales_summary = {}

with open(file_path, "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        revenue = price * quantity

        sales_summary[product] = (
            sales_summary.get(product, 0) + revenue
        )

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")

# EXERCISE 8
print("\nEXERCISE 8")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log:
    log.write(
        f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n"
    )

print("Run log updated successfully.")
