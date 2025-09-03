#-------------------------------------------------------------------------------
# Student Name: Mamoon, Iman
# Version: Python 3.X
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References:
#-------------------------------------------------------------------------------
# Any notes to grader: For example: Fully implemented
#-------------------------------------------------------------------------------
# Code starts below this line
#-------------------------------------------------------------------------------

import utils as u  # Rename to your actual utility file name (no .py)

def main():
    items = [
        'ID1,AX Jacket,202.98',
        'ID100,RJ Polo,60.99',
        'ID32,AK Tops,19.99',
        'ID34,Levis Jeans,65.57'
    ]

    # Convert strings into list of tuples: [(id, name, price), ...]
    item_list = []
    for item in items:
        parts = item.split(',')
        item_id = parts[0].strip()
        name = parts[1].strip()
        price = float(parts[2].strip())
        item_list.append((item_id, name, price))

    items_dict = u.build_item_dict(item_list)  # Call utility function
    cart = {}  # cart initialization

    print('Welcome to the IST Clothing Store!')

    while True:
        print("\n1. Display all items")
        print("2. Purchase clothes")
        print("3. Check out")
        print("0. Exit")

        user_input = input("Enter your option: ").strip()

        if user_input == '1':
            u.display_all_items(items_dict)

        elif user_input == '2':
            item_id = input("Enter the ID of the item to add: ").strip()
            try:
                quantity = int(input("Enter the quantity: ").strip())
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
            except ValueError:
                print("Invalid quantity.")
                continue

            if u.add_to_cart(item_id, quantity, cart, items_dict):
                print(f"{quantity} of {item_id} added to cart.")
            else:
                print(f"{item_id} not found. Returning to main menu.")

        elif user_input == '3':
            if not cart:
                print("Your cart is empty.")
            else:
                print("Thanks for shopping")
                print("You purchased the following item(s):")
                u.display_all_items(cart)
                total = u.check_out(cart)
                print(f"The total amount is: $ {total:.2f}")

        elif user_input == '0':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Start the program
main()
