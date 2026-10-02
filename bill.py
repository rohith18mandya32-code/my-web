cart = []
customer = ""


def menu():
    print("\n========== SMART BILLING SYSTEM ==========")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Update Quantity")
    print("4. Remove Product")
    print("5. Search Product")
    print("6. Generate Bill")
    print("7. New Bill")
    print("8. Exit")
    print("==========================================")


def add_product():
    name = input("Enter product name: ").strip()

    if name == "":
        print("Product name cannot be empty!")
        return

    for item in cart:
        if item["name"].lower() == name.lower():
            print("Product already exists!")
            print("Use Update Quantity instead.")
            return

    try:
        price = float(input("Enter price: ₹"))
        qty = int(input("Enter quantity: "))

        if price <= 0 or qty <= 0:
            print("Price and quantity must be greater than 0!")
            return

        cart.append({
            "name": name,
            "price": price,
            "qty": qty
        })

        print("Product added successfully!")

    except ValueError:
        print("Invalid price or quantity!")


def view_cart():
    if len(cart) == 0:
        print("Your cart is empty!")
        return

    print("\n============== YOUR CART ==============")
    print(f"{'No':<5}{'Product':<15}{'Price':<10}{'Qty':<6}{'Total':<10}")
    print("---------------------------------------")

    subtotal = 0

    for i, item in enumerate(cart, 1):
        total = item["price"] * item["qty"]
        subtotal += total

        print(f"{i:<5}{item['name']:<15}"
              f"{item['price']:<10.2f}"
              f"{item['qty']:<6}"
              f"{total:<10.2f}")

    print("---------------------------------------")
    print(f"Subtotal: ₹{subtotal:.2f}")


def update_quantity():
    view_cart()

    if len(cart) == 0:
        return

    try:
        number = int(input("Enter product number: "))

        if 1 <= number <= len(cart):
            qty = int(input("Enter new quantity: "))

            if qty > 0:
                cart[number - 1]["qty"] = qty
                print("Quantity updated successfully!")
            else:
                print("Quantity must be greater than 0!")
        else:
            print("Invalid product number!")

    except ValueError:
        print("Enter a valid number!")


def remove_product():
    view_cart()

    if len(cart) == 0:
        return

    try:
        number = int(input("Enter product number to remove: "))

        if 1 <= number <= len(cart):
            removed = cart.pop(number - 1)
            print(removed["name"], "removed successfully!")
        else:
            print("Invalid product number!")

    except ValueError:
        print("Enter a valid number!")


def search_product():
    name = input("Enter product name to search: ")

    found = False

    for item in cart:
        if name.lower() in item["name"].lower():
            print("\nProduct:", item["name"])
            print("Price: ₹", item["price"])
            print("Quantity:", item["qty"])
            print("Total: ₹", item["price"] * item["qty"])
            found = True

    if not found:
        print("Product not found!")


def calculate_total():
    subtotal = 0

    for item in cart:
        subtotal += item["price"] * item["qty"]

    return subtotal


def generate_bill():
    if len(cart) == 0:
        print("Cannot generate bill! Cart is empty.")
        return

    subtotal = calculate_total()

    try:
        discount = float(input("Enter discount percentage (0-100): "))

        if discount < 0 or discount > 100:
            print("Invalid discount percentage!")
            return

    except ValueError:
        print("Invalid discount!")
        return

    discount_amount = subtotal * discount / 100
    after_discount = subtotal - discount_amount

    tax = after_discount * 0.10
    grand_total = after_discount + tax

    print("\n==========================================")
    print("              FINAL INVOICE")
    print("==========================================")
    print("Customer:", customer)
    print("------------------------------------------")

    for item in cart:
        total = item["price"] * item["qty"]

        print(f"{item['name']:<15}"
              f"₹{item['price']:.2f} x {item['qty']}"
              f" = ₹{total:.2f}")

    print("------------------------------------------")
    print(f"Subtotal:        ₹{subtotal:.2f}")
    print(f"Discount ({discount}%): ₹{discount_amount:.2f}")
    print(f"After Discount:  ₹{after_discount:.2f}")
    print(f"Tax (10%):       ₹{tax:.2f}")
    print("------------------------------------------")
    print(f"GRAND TOTAL:     ₹{grand_total:.2f}")
    print("==========================================")
    print("         THANK YOU FOR SHOPPING!")
    print("==========================================")


def new_bill():
    global customer

    cart.clear()
    customer = input("Enter new customer name: ").strip()

    print("New bill created for", customer)


# MAIN PROGRAM

customer = input("Enter customer name: ").strip()

while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_cart()

    elif choice == "3":
        update_quantity()

    elif choice == "4":
        remove_product()

    elif choice == "5":
        search_product()

    elif choice == "6":
        generate_bill()

    elif choice == "7":
        new_bill()

    elif choice == "8":
        print("Thank you for using Smart Billing System!")
        break

    else:
        print("Invalid choice! Please try again.")