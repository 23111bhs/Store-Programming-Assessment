"""
Store Program by Jack Aker
This program has the sole purpose of providing a means of checking stock of items in a store and purchasing items for the consumer.
"""

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
        for item, price in available_items:
            print(item, price)

def list_items_in_budget(budget, available_items):
    for items, price in available_items:
        if price <= budget:
            print("\n--- Available items inside your specified budget: ---")
            print(items, price)
        else:
            print("There are no items inside your budget.")

def main():
    MINIMUM_BUDGET = 0

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
    
    while True:
        try:
            user_budget = float(input("Welcome to Jmart. Please enter your budget (NZD): $"))
            if user_budget <= MINIMUM_BUDGET:
                print("Please enter a valid budget.")
            else:
                display_options()
                break
        except KeyboardInterrupt:
            print("\nThank you for using this program.")
            break
        except:
            print("\nAn unexpected error has occurred. Please contact your local system administrator.")
            break
    
    while True:
        try:
            user_input = int(input("Please enter the option you would like to choose: "))
            if user_input == 1:
                display_user_budget(user_budget)
            elif user_input == 2:
                list_available_items(list_available_items)
            elif user_input == 3:
                list_items_in_budget(user_budget, available_items)
        
        except KeyboardInterrupt:
            print("\nThank you for using this program.")
            break
        except:
            print("\nAn unexpected error has occurred. Please contact your local system administrator.")
            break
main()