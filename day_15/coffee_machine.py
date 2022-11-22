from coffee_menu import MENU, resources

profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns true if order can be made, returns false if resources insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, cost_of_drink):
    """Return true when payment is accepted or false when money is insufficient"""
    if money_received >= cost_of_drink:
        ##  If the user has inserted too much money, the machine should offer change.
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources"""
    for item in order_ingredients:
        resources[item] - order_ingredients[item]
    print(f"Here is your {drink_name}")

is_machine_on = True
# Machine powered on
while is_machine_on:
# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    ## Check the user’s input to decide what to do next.
    # Turn off the Coffee Machine by entering “off” to the prompt.
    if selection == 'off':
        is_machine_on = False
        print("Powering off Machine...")
    elif selection == 'report':

        # Print report.
        ## When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
        # Water: 100ml
        # Milk: 50ml
        # Coffee: 76g
        # Money: $2.5
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[selection]

        # Check resources sufficient?
        ## When the user chooses a drink, the program should check if there are enough resources to make that drink.
        ## E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
        ## The same should happen if another resource is depleted, e.g. milk or coffee.
        if is_resource_sufficient(drink["ingredients"]):

            # Process coins.
            ## If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
            ## Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
            ## Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
            payment = process_coins()

            # Check transaction successful?
            ## Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
            # program should say “Sorry that's not enough money. Money refunded.”.
            ## But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
            # Water: 100ml
            # Milk: 50ml
            # Coffee: 76g
            # Money: $2.5
            if is_transaction_successful(payment, drink["cost"]):
               make_coffee(selection, drink["ingredients"])

## The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.




