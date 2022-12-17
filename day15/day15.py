# Coffee Machine
from menu import MENU


def give_change(change):
    if change == 0:
        print("There is no money for change.")
    else:
        print(f"Here is your change: ${round(change,2)}")


def sufficient_resources(resources, ingredients):
    """Check the sufficiency of the resources"""
    for i in resources:
        if resources[i] < ingredients[i]:
            print(f"Sorry, there is not enough {i} in the machine.")
            return False
    return True


def sum_money(quarters, dimes, nickles, pennies):
    return 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies


def sufficient_money(money, cost):
    if money < cost:
        return False
    return True


def make_coffee(resources, ingredients):
    """Subtracts the ingredients from the resources"""
    for i in resources:
        resources[i] -= ingredients[i]


resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}
money = 0

while True:
    main_menu = input(
        "\nType 'report' to see the resources left at the machine\nType 'change' to take change back\nType 'menu' to see and order drinks\nType 'off' to turn the machine off\n").lower()
    if main_menu == "off":
        break
    elif main_menu == "menu":
        order = input(
            f"Espresso - ${MENU['espresso']['cost']}\nLatte - ${MENU['latte']['cost']}\nCappuccino - ${MENU['cappuccino']['cost']}\nWhat would you like to have? ").lower()
        if sufficient_resources(resources, MENU[order]['ingredients']):
            while not sufficient_money(money, MENU[order]['cost']):
                print(f"You have ${money}, it's not enough.")
                quarters = float(input("Please insert coins.\nHow many quarter ($0.25)? "))
                dimes = float(input("How many dimes ($0.1)? "))
                nickles = float(input("How many nickles ($0.05)? "))
                pennies = float(input("How many pennies ($0.01)? "))
                money += sum_money(quarters, dimes, nickles, pennies)
            make_coffee(resources, MENU[order]['ingredients'])
            money -= MENU[order]['cost']
            print(f"Enjoy your {order} ☕")
    elif main_menu == "report":
        print(f"Resources in the machine:\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    elif main_menu == "change":
        give_change(money)
        money = 0
