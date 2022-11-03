MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order):
    for item in order:
        if(order[item]>resources[item]):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

coffee_work=True
while coffee_work:
    requirement = input("What would you like? (espresso/latte/cappuccino): ")
    if requirement=="off":
        coffee_work=False
        print("Coffee Machine Turned Off")
    elif requirement=="report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${round(profit,2)}")
    elif check_resources(MENU[requirement]["ingredients"]):
        quarters = int(input("Quarters Here: "))
        dimes = int(input("Dimes Here: "))
        nickles = int(input("Nickles Here: "))
        pennies = int(input("Pennies Here: "))
        money = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
        if money<MENU[requirement]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            coffee_work = False
        else:
            for item in MENU[requirement]["ingredients"]:
                resources[item]-= MENU[requirement]["ingredients"][item]
            if money>MENU[requirement]["cost"]:
                profit+=money-MENU[requirement]["cost"]
            print(f"“Here is your {requirement}. Enjoy!")