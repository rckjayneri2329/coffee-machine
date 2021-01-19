from data import MENU, resources
machine_offline = False
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
        print(MENU[order]["ingredients"])
    else:
        print("Invalid Choice. Try again.")