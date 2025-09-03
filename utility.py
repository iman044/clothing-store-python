#-------------------------------------------------------------------------------
# Student Name: Last name, first name
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
#----------------------------------------------------------------------------

def build_item_dict(items):
    ''' Returns item_dict from items list. '''
    item_dict = {}
    for item in items:
        item_id, name, price = item
        item_dict[item_id] = [name, price]
    return item_dict


def check_out(cart):
    ''' Returns total price from cart dictionary'''
    total = 0
    for item in cart.values():
        price = item[-2]
        quantity = item[-1]
        total += price * quantity
    return total


def display_all_items(d):
    ''' Display each dictionary key and value'''
    print(f"{'ID':<6} {'Item Name':<15} {'Price':<10} {'Qty':<5}")
    print("-" * 40)
    for item_id, values in d.items():
        name = values[0]
        price = values[1]
        qty = values[2] if len(values) == 3 else ''
        print(f"{item_id:<6} {name:<15} {price:<10} {qty:<5}")


def add_to_cart(item_id, item_qty, cart, item_dict):
    '''Add an item to cart if ID exists. Returns True if added
    otherwise returns False'''
    if item_id in item_dict:
        name, price = item_dict[item_id]
        if item_id in cart:
            cart[item_id][2] += item_qty  # Increase existing quantity
        else:
            cart[item_id] = [name, price, item_qty]  # Add new item
        return True
    else:
        return False
