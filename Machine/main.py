from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

request = ""

coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
mymenu = Menu()

while request!="off":
    request = input("What would you like? (espresso/latte/cappuccino/):")
    if request == "off":
        break
    elif request=="report":
        coffeemaker.report() 
        moneymachine.report()
    else:
        drink = mymenu.find_drink(request)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)



