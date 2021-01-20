from data import COINS, MENU, resources

machine_offline = False
resource_checked = ''
monetary_value = 0


def add_profit(order_cost):
    resources["money"] += order_cost


def deduct_resources(order_type):
    for ingredient in MENU[order_type]['ingredients']:
        resources[ingredient] -= MENU[order_type]['ingredients'][ingredient]


def make_coffee():
    print("make coffee")


def is_resources_sufficient(order_ingredients):
    enough_resources = True
    for ingredient in order_ingredients:
        if resources[ingredient] < order_ingredients[ingredient]:
            enough_resources = False
            break
    return enough_resources


def process_coins():
    print("Please insert coins.")
    inserted_coins = 0
    total_coins = 0
    for coin_type in COINS:
        inserted_coins = float(input(f"how many {coin_type}?: "))
        total_coins = total_coins + (inserted_coins * COINS[coin_type])
    return total_coins


def check_transaction(inserted_coins_total, order_type):
    result = inserted_coins_total - MENU[order_type]['cost']

    if inserted_coins_total < MENU[order_type]["cost"]:
        result_message = "Sorry that's not enough money. Money refunded."
    else:
        if inserted_coins_total > MENU[order_type]["cost"]:
            change = inserted_coins_total - MENU[order_type]['cost']
            result_message = f"Here is ${change:.2f} in change.\n"
        result_message += f"Here is your {order_type} ☕. Enjoy!"

    return result


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
order = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
if order == 'off':
    machine_offline = True

# TODO: 3. Print report.
elif order == 'report':
    for resource in resources:
        print(f"{resource.title()}: {resources[resource]}")

else:
    if order in MENU:

        # TODO: 4. Check resources sufficient.
        if is_resources_sufficient(MENU[order]["ingredients"]):

            # TODO: 5. Process coins.
            monetary_value = process_coins()
            print(f"{monetary_value:.2f}")

            # TODO: 6. Check transaction successful.
            print(check_transaction(monetary_value, order))
        else:
            print(f"Sorry there is not enough {resource_checked}.")
        print(MENU[order]["ingredients"])
        print(resources)
        print(resource_checked)
    else:
        print("Invalid choice")
