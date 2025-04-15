import csv

products = list()
stock = list()
result_list = []

with open("./thrd_coding - Sheet1.csv", mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        products.append(row)

with open("./stock - Sheet1.csv", mode='r') as file:
    stock_csv_reader = csv.DictReader(file)
    for row in stock_csv_reader:
        stock.append(row)


for product,s in zip(products,stock):
    value_change = "*"
    action = 0.1
    if int(product["stock"]) < 20 and int(s["quantity_sold"]) > 30:
        value_change = "*"
        action = 0.15
    elif int(product["stock"]) > 200 and int(s["quantity_sold"]) == 0:
        value_change = "%"
        action = 0.30
    elif int(product["stock"]) > 100 and int(s["quantity_sold"]) < 20:
        value_change = "%"
        action = 0.10

    if value_change == "%":
        new_price = int(product["cost_price"]) % action
    else:
        new_price = int(product["cost_price"]) * action

    if not new_price > (int(product["cost_price"]) * 0.20):
        new_price = int(product["cost_price"]) * 1.2

    result_list.append({"sku":product["sku"],"old_price":product["cost_price"],"new_price":round(new_price,2)})

print(result_list)

with open('price_update.csv', mode='w', newline='') as file:
    # Define the column headers
    fieldnames = ['sku', 'old_price', 'new_price']

    # Create the DictWriter object
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header (column names)
    writer.writeheader()

    # Write the data rows
    writer.writerows(result_list)