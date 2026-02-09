recipes = {
    "small": {
        "ingredients": {
            "bread": 2,
            "ham": 4,
            "cheese": 4,
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,
            "ham": 6,
            "cheese": 8,
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,
            "ham": 8,
            "cheese": 12,
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,
    "ham": 18,
    "cheese": 24,
}


class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print("Sorry there is not enough " + item + ".")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        large = int(input("how many large dollars?: "))
        half = int(input("how many half dollars?: "))
        quarter = int(input("how many quarters?: "))
        nickel = int(input("how many nickels?: "))
        total = large * 1.0 + half * 0.5 + quarter * 0.25 + nickel * 0.05
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            print("Here is $" + str(change) + " in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(sandwich_size + " sandwich is ready. Bon appetit!")


machine = SandwichMachine(resources)

while True: 
    choice = input("What would you like? (small / medium / large / quit / info): ")
    
    if choice == "quit":
        break
    elif choice == "info":
        print("Bread: " + str(resources["bread"]) + " slice(s)")
        print("Ham: " + str(resources["ham"]) + " slice(s)")
        print("Cheese: " + str(resources["cheese"]) + " pound(s)")
    elif choice in ["small", "medium", "large"]:
        sandwich = recipes[choice]
        if machine.check_resources(sandwich["ingredients"]):
            payment = machine.process_coins()
            if machine.transaction_result(payment, sandwich["cost"]):
                machine.make_sandwich(choice, sandwich["ingredients"])