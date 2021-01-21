from data import COINS, MENU, resources

machine_online = True
monetary_value = 0
resource_checked = []


def add_profit(order_cost):
    resources["money"] += order_cost


def deduct_resources(order_type):
    for ingredient in MENU[order_type]["ingredients"]:
        resources[ingredient] -= MENU[order_type]["ingredients"][ingredient]


def check_resources(order_ingredients):
    insufficient_ingredients = []
    for ingredient in order_ingredients:
        if resources[ingredient] < order_ingredients[ingredient]:
            insufficient_ingredients.append(ingredient)
    result_message = ', '.join(insufficient_ingredients)
    return result_message


def process_coins():
    print("Please insert coins.")
    total_coins = 0
    for coin_type in COINS:
        inserted_coins = float(input(f"how many {coin_type}?: "))
        total_coins = total_coins + (inserted_coins * COINS[coin_type])
    return total_coins


def make_coffee(inserted_coins_total, order_type):
    change = inserted_coins_total - MENU[order_type]["cost"]
    result_message = ""
    if change > 0:
        result_message = f"Here is ${change:.2f} in change.\n"
    result_message += f"Here is your {order_type} ☕. Enjoy!"

    return result_message


def is_transaction_successful(inserted_coins_total, order_type):
    successful_transaction = True
    result = inserted_coins_total - MENU[order_type]["cost"]

    if result < 0:
        successful_transaction = False

    return successful_transaction


def report_resource():
    for resource in resources:
        print(f"{resource.title()}: {resources[resource]}")


while machine_online:

    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        machine_online = False

    elif order == "report":
        report_resource()

    else:
        if order in MENU:

            resource_checked = check_resources(MENU[order]["ingredients"])
            if resource_checked == "":

                monetary_value = process_coins()
                print(f"{monetary_value:.2f}")

                if is_transaction_successful(monetary_value, order):
                    add_profit(MENU[order]["cost"])

                    print(make_coffee(monetary_value, order))

                    deduct_resources(order)

                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Sorry there is not enough {resource_checked}.")
        else:
            print("Invalid choice")
