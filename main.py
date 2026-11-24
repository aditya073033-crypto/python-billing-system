def shopping_billing_system():
    # Dictionary storing product names and prices in Rupees (₹)
    menu = {
        "Laptop": 45000,
        "Headphones": 1500,
        "Keyboard": 1200,
        "Mouse": 800,
        "Backpack": 2200,
        "Water Bottle": 500
    }

    print("--- Available Products ---")
    for product, price in menu.items():
        print(f"{product}: ₹{price}")
    print("--------------------------\n")

    cart = {}

    # Allow customer to select multiple products and quantities
    while True:
        choice = input("Enter the product name you want to buy (or type 'done' to finish): ").strip()
        if choice.lower() == 'done':
            break

        # Matching input product with dictionary keys (case-insensitive search)
        matched_product = None
        for product in menu:
            if product.lower() == choice.lower():
                matched_product = product
                break

        if matched_product:
            try:
                quantity = int(input(f"Enter quantity for {matched_product}: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

                # Accumulate quantity if product is selected multiple times
                if matched_product in cart:
                    cart[matched_product] += quantity
                else:
                    cart[matched_product] = quantity
            except ValueError:
                print("Invalid input! Please enter a valid whole number for quantity.")
        else:
            print("Product not found! Please choose from the list.")

    if not cart:
        print("No items selected. Thank you for visiting!")
        return

    # Calculate the total bill
    total_bill = 0
    print("\n--- Your Invoice ---")
    for product, qty in cart.items():
        cost = menu[product] * qty
        total_bill += cost
        print(f"{product} x {qty} = ₹{cost}")

    print(f"Subtotal: ₹{total_bill}")

    # Apply 10% discount if the total exceeds ₹2,000
    if total_bill > 2000:
        discount = total_bill * 0.10
        final_bill = total_bill - discount
        print(f"Discount (10%): -₹{discount:.2f}")
        print(f"Total Bill to Pay: ₹{final_bill:.2f}")
    else:
        print(f"Total Bill to Pay: ₹{total_bill:.2f}")

# Run the shopping billing system
shopping_billing_system()