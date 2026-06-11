"""
Store Program by Jack Aker
This program has the sole purpose of providing a means of checking stock of items in a store and purchasing items for the consumer.
"""

import sys

def display_options():
    print("\n---- Store Program ----")
    print("1: View your budget")
    print("2: List available items")
    print("3: List all items in your budget")
    print("4: Buy item")
    print("5: List purchased items")
    print("6: Exit\n")


def display_user_budget(budget):
    print(f"\nYour budget is: ${budget:.2f}\n")

def list_available_items(available_items):
    if not available_items:
        print("\nThere are no items left.\n")
    else:
        for item, price in available_items.items():
            print(item, price)
        print()

def list_items_in_budget(budget, available_items):
    print()
    for items, price in available_items.items():
        if price <= budget:
            print(items, price)
    print()

def list_items_already_bought(purchased_items):
    print("\nHere is your current recipt.")
    for item, price in purchased_items.items():
        print(f"- {item}, ${price:.2f}")
    print()

def buy_item(budget, available_items, purchased_items, current_total_price):
    try:
        current_total_price = 0.00
        list_available_items(available_items)
        chosen_item = input("Please enter the name of the item you would like to buy: ")
        chosen_item_cleaned = ''.join(char for char in chosen_item if char.isalnum() or char.isspace()).strip()

        matched_key = None
        for item_name in available_items:
            if item_name.lower() == chosen_item_cleaned.lower():
                matched_key = item_name

        if matched_key:
            price = available_items[matched_key]
            if budget >= price:
                purchased_items[matched_key] = price
                del available_items[matched_key]
                budget -= price
                current_total_price += price
                print(f"\nSuccessfully bought {matched_key}! Your total cart price is now: ${current_total_price:.2f} and your budget remaining is ${budget:.2f}\n")
            else:
                print(f"\nYou are unable to afford this item. The item costs: ${price:.2f}, and your budget is: ${budget:.2f}\n")
        else:
            print("\nPlease select an item in our stock.\n")
        return budget, purchased_items, current_total_price
    except ValueError:
        print("\nPlease enter the full name of the item.\n")
    except KeyboardInterrupt:
        print("\nThank you for using this program. Exiting now...")
        sys.exit()

def main():
    MINIMUM_BUDGET = 0
    current_total_price = 0.00

    available_items = {
        "Mouse": 25.00,
        "Keyboard": 35.75,
        "Headphones": 39.99,
        "Webcam": 60.00,
        "Speakers": 45.30,
        "USB Drive": 15.00,
        "SSD Drive": 94.99,
        "HDMI Cable": 12.30,
        "Ethernet Cable": 10.00,
        "Mouse Pad": 10.00,
        "Laptop Sleeve": 25.00,
        "Cooling Pad": 30.00,
        "USB Hub": 20.00,
        "Power Bank": 49.98,
        "SD Card": 20.00,
        "Card Reader": 18.50,
        "Desk Fan": 22.00,
        "Screen Cleaner": 15.00,
        "Power Board": 28.00,
        "USB Adapter": 14.99
    }

    purchased_items = {}
    
    while True:
        try:
            user_budget = float(input("Welcome to Jmart. Please enter your budget (NZD): $"))
            if user_budget <= MINIMUM_BUDGET:
                print("\nPlease enter a valid budget.\n")
            else:
                display_options()
                break
        except KeyboardInterrupt:
            print("\nThank you for using this program. Exiting now...")
            sys.exit()
        except:
            print("\nAn unexpected error has occurred. Please contact your local system administrator.")
            break
    
    while True:
        try:
            user_input = int(input("Please enter the option you would like to choose: "))
            if user_input == 1:
                display_user_budget(user_budget)
            elif user_input == 2:
                if not available_items:
                    print("\nThere are no items left in stock.")
                else:
                    list_available_items(available_items)
            elif user_input == 3:
                if not available_items:
                    print("\nThere are no items left in stock.")
                list_items_in_budget(user_budget, available_items)

            elif user_input == 4:
                if not available_items:
                    print("\nThere are no items left in stock.")
                else:
                    user_budget, purchased_items, current_total_price = buy_item(user_budget, available_items, purchased_items, current_total_price)
            elif user_input == 5:
                if not purchased_items:
                    print("You haven't purchased anything.")
                else:
                    list_items_already_bought(purchased_items)

            elif user_input == 6:
                break
        
        except KeyboardInterrupt:
            print("\nThank you for using this program. Exiting now...")
            sys.exit()
        # except:
        #     print("\nAn unexpected error has occurred. Please contact your local system administrator.")
        #     break
main()