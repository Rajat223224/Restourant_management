# Define initial inventory
inventory = {'Dhosa': 10, 'Paneer_Rise': 15, 'Manchurian': 20, 'omlate': 10}

# Define menu items and prices
menu = {'Dhosa': 10, 'Paneer_Rise': 15, 'Manchurian': 5, 'omlate': 7}

# Define order dictionary
orders = {}

# Define function to display menu
def display_menu():
    print('Menu:')
    for item, price in menu.items():
        print(f'{item}: ${price}')

# Define function to place an order
def place_order():
    item = input('Enter menu item: ')
    if item in menu:
        quantity = int(input('Enter quantity: '))
        if inventory[item] < quantity:
            print(f'Sorry, we only have {inventory[item]} {item}s left.')
        else:
            orders[item] = orders.get(item, 0) + quantity
            inventory[item] -= quantity
            print(f'Added {quantity} {item}(s) to your order.')
    else:
        print('Sorry, that item is not on the menu.')

# Define function to display current order
def display_order():
    print('Current Order:')
    for item, quantity in orders.items():
        print(f'{item}: {quantity}')

# Define function to calculate total cost
def calculate_total():
    total = sum(orders[item] * menu[item] for item in orders)
    return total

# Define function to generate bill
def generate_bill():
    print('Bill:')
    display_order()
    total = calculate_total()
    print(f'Total: ${total:.2f}')

# Main loop
while True:
    print('\nOptions:')
    print('1. Display menu')
    print('2. Place order')
    print('3. Display current order')
    print('4. Generate bill')
    print('5. Quit')
    choice = input('Enter choice (1-5): ')
    if choice == '1':
        display_menu()
    elif choice == '2':
        place_order()
    elif choice == '3':
        display_order()
    elif choice == '4':
        generate_bill()
    elif choice == '5':
        break
    else:
        print('Invalid choice. Please try again.')
