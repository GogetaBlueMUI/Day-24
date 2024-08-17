inventory = []

def add_product():
    name = input("Enter product name: ").strip()
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    for product in inventory:
        if product['name'].lower() == name.lower():
            print("Product already exists. Use update to change quantity.")
            return
    product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(product)
    print("Product added successfully.")

def update_quantity():
    name = input("Enter product name to update: ").strip()
    new_quantity = int(input("Enter new quantity: "))
    for product in inventory:
        if product['name'].lower() == name.lower():
            product['quantity'] = new_quantity
            print(f"Quantity for product '{name}' updated to {new_quantity}.")
            return
    print("Product not found.")

def display_inventory():
    if not inventory:
        print("No products in inventory.")
    else:
        for product in inventory:
            print(f"Name: {product['name']}, Price: ${product['price']:.2f}, Quantity: {product['quantity']}")

while True:
    print("\n1. Add Product")
    print("2. Update Quantity")
    print("3. View Inventory")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == '1':
        add_product()
    elif choice == '2':
        update_quantity()
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
