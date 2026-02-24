total = 0

print("Enter details for 5 items:")
for i in range(1, 6):
    price = float(input(f"Price of item {i}: "))
    qty = int(input(f"Quantity of item {i}: "))
    total += (price * qty)

# Calculate discount (10% if total > 100, else 0)
discount = total * 0.10 if total > 100 else 0
final_amount = total - discount

# Display final results
print("\n--- Billing Summary ---")
print(f"Original Total: Rs. {total}")
print(f"Discount: Rs. {discount}")
print(f"Final Payable Amount: Rs. {final_amount}")