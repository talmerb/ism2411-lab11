# Reflection 1: I would use .get() for optional information, such as a customer's
# phone number, when a missing value should have a reasonable default. I would use
# bracket notation for required information so a missing key reveals a problem.
# My rule of thumb is .get() for optional fields and brackets for required fields.
#
# Reflection 2: Accumulating sales by region reminds me of an Excel PivotTable
# or SUMIF, which groups records and totals their amounts. Python can repeat this
# process automatically across large datasets and files without manually updating
# spreadsheet formulas or ranges.

# Exercise 1: One customer
print("Exercise 1")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2: Update and add
print("\nExercise 2")
customer["phone"] = "555-0101"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# Exercise 3: Safe lookup
print("\nExercise 3")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError: {error}")

# Exercise 4: Iterate
print("\nExercise 4")
for key, value in customer.items():
    print(f"{key}: {value}")
# Direct iteration returns keys; .items() returns key-value pairs.
for key in customer:
    print(f"{key}: {customer[key]}")

# Exercise 5: Lookup table
print("\nExercise 5")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = 200 * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")

# Exercise 6: List of dicts
print("\nExercise 6")
customers = [
    customer,
    {"name": "Ben", "email": "ben@example.com", "tier": "silver", "ytd_spend": 450},
    {"name": "Cara", "email": "cara@example.com", "tier": "bronze", "ytd_spend": 100},
]
for current_customer in customers:
    rate = tier_discounts.get(current_customer["tier"], 0)
    discount_amount = 300 * rate
    print(
        f"{current_customer['name']} | {current_customer['tier']} | "
        f"Discount on $300: ${discount_amount:.2f}"
    )

# Exercise 7: Nested catalog
print("\nExercise 7")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} — {details['stock']} remaining")

# Exercise 8: Sales by region
print("\nExercise 8")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for transaction in transactions:
    region = transaction["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + transaction["amount"]
for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
