import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True
    while is_on:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print("Bread: " + str(resources['bread']) + " slice(s)")
            print("Ham: " + str(resources['ham']) + " slice(s)")
            print("Cheese: " + str(resources['cheese']) + " ounce(s)")
        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()