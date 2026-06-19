"""
Store Program by Jack Aker | started Jun 9th ending Jun 19th.
This program has the sole purpose of providing a means of checking stock of items in a store and purchasing items for the consumer.
"""

# import sys package so that i can use 'sys.exit()' to exit the program easily.
import sys

# define the options that the user will need to choose for the program. when this function is called, the options will be printed in the terminal for the user to see.
def display_options(budget,avail_items,items_budget,buy_item,bought_item,cart_total,help,exit):
    print("\n---- Store Program ----")
    print(f"{budget}: View your budget")
    print(f"{avail_items}: List available items")
    print(f"{items_budget}: List all items in your budget")
    print(f"{buy_item}: Buy item")
    print(f"{bought_item}: List purchased items")
    print(f"{cart_total}: Show currrent cart total")
    print(f"{help}: Display this menu again")
    print(f"{exit}: Exit the program\n")

# display the user's remaining budget for their shopping session. when this function is called, it takes one value (budget) and displays it in float form (:.2f) for the user.
def display_user_budget(budget):
    print(f"\nYour remaining budget is: ${budget:.2f}\n")

# this function takes one value upon being called and converts it to float form (:.2f) for the user.
def show_current_cart_total(current_total_price):
    # if the current total price of the user's cart exists (is over 0.01), then display the below text.
    if current_total_price:
        print(f"\nThe current total of all your items is: ${current_total_price:.2f}\n")
    # if the current total price of the user's cart does NOT exist, display the message below informing them to purchase an item first.
    else:
        print(f"\nYou haven't purchased anything. Please purchase an item to check your cart total.\n")

# this function has the use of displaying the currently in-stock items inside of the available_items dictionary.
def list_available_items(available_items):
    # if there are no items inside of the dictionary, display 'There are no items left.' in the terminal for the user.
    if not available_items:
        print("\nThere are no items left.\n")
    
    # if the dictionary has items inside of it, loop through the items with the item name and item price and display it for the user. 
    else:
        for item, price in available_items.items():
            print(f"- {item}, ${price:.2f}")
        print()

# this function has the use of showing the items that fit inside of the user's budget and displays it for the user.
def list_items_in_budget(budget, available_items):
    # display extra line before loop to make the program's output easier to read for the user.
    print()
    
    # use boolean T/F value to check if the user cannot afford anything in the dictionary, if they can, the program displays the items they can purchase.
    can_afford_items = False
    for item, price in available_items.items():
        if price <= budget:
            print(f"- {item}, ${price:.2f}")
            can_afford_items = True

    if not can_afford_items:
        print("You cannot afford anything in stock.")
    
    # display another line after loop to make the program's output easier to read for the user.    
    print()

# this function has the use of showing the items that the user has already bought and then displaying them for the user.
def list_items_already_bought(purchased_items):
    # loop through the items in purchased_items and seperate the key/values so that when an item is in the dictionary, it will print the item and price in float form (:.2f)
    print("\nHere is your current recipt.")
    for item, price in purchased_items.items():
        print(f"- {item}, ${price:.2f}")
    
    # display extra line after loop to make the program's output easier to read for the user.
    print()

# this function has the use of allowing the user to buy an item in an interactive way while returning values to user.
def buy_item(budget, available_items, purchased_items, current_total_price):

    try:
        cheapest_item_available = min(available_items.values()) # sort through the values of available_items and find the lowest value.
        if budget < cheapest_item_available: # if the user's budget is less than the cheapest item, print the below text and end the function.
            print(f"\nYou cannot afford any items in stock. The cheapest item costs: ${cheapest_item_available:.2f}, and you have {budget:.2f}\n")
            return budget, purchased_items, current_total_price # if the user cannot afford any items, return them to the options menu.
    
    except:
        print("\nAn unexpected error has occurred. Please contact your local system administrator.")
        sys.exit() # gracefully quit program upon unexpected error

    # display available items to the user once the function is called.
    list_available_items(available_items)

    # loop through the item buying process until the user enters a valid item name
    while True:
        try:
            # define user input section where the user can input the item that they would like to purchase.
            chosen_item = input("Please enter the name of the item you would like to buy (or enter 'exit' to exit): ")

            if chosen_item == "exit":
                print()
                return budget, purchased_items, current_total_price

            # clean the user's input by using a for-loop that iterates through all the characters in the input and stripping anything except what the program needs.
            chosen_item_cleaned = ''.join(char for char in chosen_item if char.isalnum() or char.isspace()).strip()

            matched_key = None
            checked_item = 0

            # loop through available_items' keys until the user's input has been matched. if it matches, set 'matched_key' to that key. if not, catch error below and print 'please select an item in our stock.'
            for item_name in available_items: 
                if item_name.lower() == chosen_item_cleaned.lower(): # match the item name with the cleaned user input in lower form.
                    matched_key = item_name # set matched_key as the item name if the user's inputted item and the current item in the loop match.
                    break # we use a break so that once the item is found, the for loop ends for efficiency.

            # if the key exists, set 'price' to the value of matched_key.
            if matched_key:
                price = available_items[matched_key]
        
            # check if the user can afford the item and if they can, add the item to the purchased_items dict,
            # then remove the item from available_items, subtract the price from the budget, and add the price of the item to the 'current_total_price' variable.
                print()
                while True:
                    user_confirmation = input(f"The {matched_key} costs ${price:.2f}. Would you like to continue? (Y/N): ").lower().strip()

                    if user_confirmation == "y":
                        checked_item = 1 # set variable to '1' for the first case (yes) and break out of the while loop so that the selected item can be purchased.
                        break

                    elif user_confirmation == "n":
                        print(f"\n{matched_key} not bought.\n")
                        checked_item = 2 # set variable to '2' for the second case (no) so that further down on line 147 i can use it to 'pass' instead of hitting the else on ln 149.
                        break

                    else: # if the user_confirmation is anything other than 'y' or 'n' then display the message below.
                        print(f"\nPlease enter 'Y'(es) or 'N'(o).\n")

                if budget >= price and checked_item == 1:
                    purchased_items[matched_key] = price
                    del available_items[matched_key]
                    budget -= price
                    current_total_price += price
                    print(f"\nSuccessfully bought {matched_key}! Your total cart price is now: ${current_total_price:.2f} and your remaining budget is ${budget:.2f}\n")
                    
                    # only return the budget if a valid item is chosen, the user can afford it, and no other errors have been thrown.
                    return budget, purchased_items, current_total_price

                # if the user cannot afford their selected item, inform them of the cost and the budget.

                elif checked_item == 2:
                    continue

                else:
                    print(f"\nYou are unable to afford this item. The item costs: ${price:.2f}, and your budget is: ${budget:.2f}\n")

            # if the item chosen does not exist inside of available_items, inform the user of their mistake.
            else:
                print("\nPlease select an item in our stock.\n")

        except ValueError:
            print("\nPlease enter the full name of the item.\n")

        except KeyboardInterrupt:
            print("\nThank you for using this program. Exiting now...")
            sys.exit()

        except:
            print("\nAn unexpected error has occurred. Please contact your local system administrator.")
            sys.exit()


# define main function which calls other functions and stores main values alongside the item stock.
def main():
    # constant values for the display menu to use instead of hard-coding the values that will be used/displayed on launch.
    MINIMUM_BUDGET = 0 # define a static value designed NOT to be changed unless need. this value sets the minimum budget needed for a user
    SHOW_BUDGET_OPTION = 1
    AVAILABLE_ITEMS_OPTION = 2
    ITEMS_IN_BUDGET_OPTION = 3
    BUY_ITEM_OPTION = 4
    BOUGHT_ITEMS_OPTION = 5
    CART_TOTAL_OPTION = 6
    SHOW_HELP_MENU_OPTION = 7
    EXIT_PROGRAM_OPTION = 8 # static value for the exit option which allows the user to exit the program.

    # float variable to store the total price of all the user's items.
    current_total_price = 0.00 # define a variable which stores the current total cart price.

    available_items = { # define a dictionary which stores all in-stock items at the time
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

    purchased_items = {} # define dictionary which will store the purchased items that the user chooses.
    
    # loop through the budget part of the program until the user inputs their allowed budget (0.01 - inf).
    while True:
        # use a 'try catch' to not throw an error in the terminal when unexpected input is entered.
        try:
            user_budget = float(input("Welcome to Jmart. Please enter your budget (NZD): $"))
            if user_budget <= MINIMUM_BUDGET:
                print("\nPlease enter a valid budget.\n")

            else:
                display_options(SHOW_BUDGET_OPTION,AVAILABLE_ITEMS_OPTION,ITEMS_IN_BUDGET_OPTION,BUY_ITEM_OPTION,BOUGHT_ITEMS_OPTION,CART_TOTAL_OPTION,SHOW_HELP_MENU_OPTION,EXIT_PROGRAM_OPTION)
                break

        # if the user force quits the program (ctrl + c or ctrl + a, ctrl + c) the program will gracefully quit instead of throwing an error in the terminal.
        except KeyboardInterrupt:
            print("\nThank you for using this program. Exiting now...")
            sys.exit()

        # if a user enters anything other than a float or integer, the program will output 'Please enter a numeric value (1, 10.00, 50).'
        except ValueError:
            print("\nPlease enter a numeric value (1, 10.00, 50).\n")

        # in the event that something unimagineable happens, catch any other errors and gracefully quit the program
        except:
            print("\nAn unexpected error has occurred. Please contact your local system administrator.")
            sys.exit()
    
    # loop through the option selection part of the program (1-7)
    while True:
        try:
            user_input = int(input("Please enter the option you would like to choose (or enter '7' to display options again): "))
            # if the user selects option 1 then call the 'display_user_budget' function to display their budget
            if user_input == SHOW_BUDGET_OPTION:
                display_user_budget(user_budget)

            # calls function to list items that the user can purchase. if there are none, output 'There are no items left in stock.
            elif user_input == AVAILABLE_ITEMS_OPTION:
                if not available_items:
                    print("\nThere are no items left in stock.")
                else:
                    list_available_items(available_items)

            # if the user inputs 3, then call function which lists all items inside of their budget.
            elif user_input == ITEMS_IN_BUDGET_OPTION:
                if not available_items:
                    print("\nThere are no items left in stock.\n")
                list_items_in_budget(user_budget, available_items)

            # if the user inputs 4, then call function which allows a user to buy an item and return values to main function.
            elif user_input == BUY_ITEM_OPTION:
                if not available_items:
                    print("\nThere are no items left in stock.\n")
                else:
                    user_budget, purchased_items, current_total_price = buy_item(user_budget, available_items, purchased_items, current_total_price)
                    if purchased_items:
                        list_items_already_bought(purchased_items)

            # if the user inputs 5, check if the user has bought any items and if they have, display them.
            elif user_input == BOUGHT_ITEMS_OPTION:
                if not purchased_items:
                    print("\nYou haven't purchased anything.\n")
                else:
                    list_items_already_bought(purchased_items)

            # if the user inputs 6, output their current cart total.
            elif user_input == CART_TOTAL_OPTION:
                show_current_cart_total(current_total_price)

            # if the user inputs 7, display the numbered options again in the terminal.
            elif user_input == SHOW_HELP_MENU_OPTION:
                display_options(SHOW_BUDGET_OPTION,AVAILABLE_ITEMS_OPTION,ITEMS_IN_BUDGET_OPTION,BUY_ITEM_OPTION,BOUGHT_ITEMS_OPTION,CART_TOTAL_OPTION,SHOW_HELP_MENU_OPTION,EXIT_PROGRAM_OPTION)
            
            # if the user inputs 8, break out of this while True loop and show their recipt.
            elif user_input == EXIT_PROGRAM_OPTION:
                break

            else:
                print("\nPlease select a valid option.\n")

        # if the user tries to force exit the program, exit gracefully and dipslay a 'goodbye' message.
        except KeyboardInterrupt:
            print()
            print("\nThank you for using this program. Exiting now...\n")
            sys.exit()

        # if a user does not input an integral value for the selection process, display 'Please select an option in numeric form.'
        except ValueError:
            print("\nPlease select an option in numeric form.\n")

        # if there is any other error which has not been specified, inform the user to contact a systems administrator.
        except:
            print("\nAn unexpected error has occurred. Please contact your local system administrator.")
            break
    
    try:
        if not purchased_items:
            print("\nYou have not purchased anything.\n")
        else: 
            list_items_already_bought(purchased_items)
        print("\nThank you for shopping at Jmart!")

    # catch all errors and display the message below in the terminal if something completely unexpected happens.
    except:
        print("\nAn unexpected error has occurred. Please contact your local system administrator.")

main()
