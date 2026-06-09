"""
Store Program by Jack Aker
This program has the sole purpose of providing a means of checking stock of items in a store and purchasing items for the consumer.
"""

def display_options():
    print("1: View your budget")
    print("2: List available items")
    print("3: List all items in your budget")
    print("4: Buy item")
    print("5: List purchased items")
    print("6: Exit")

def main():
    display_options()

    try:
        while True:
            user_input = int(input("Please enter the option you would like to choose: "))

    except KeyboardInterrupt:
        print("Thank you for using this program.")
    except:
        print("An unexpected error has occurred. Please contact your local system administrator.")

main()