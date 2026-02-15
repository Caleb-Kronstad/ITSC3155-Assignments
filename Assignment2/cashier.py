class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickels?: "))
        pennies = int(input("how many pennies?: "))
        total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print("Here is $" + str(change) + " in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False