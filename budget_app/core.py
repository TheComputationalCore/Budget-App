class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": float(amount), "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": -float(amount), "description": description}
            )
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": -float(amount), "description": f"Transfer to {category.name}"}
            )
            category.ledger.append(
                {
                    "amount": float(amount),
                    "description": f"Transfer from {self.name}",
                }
            )
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}"[:7].rjust(7)
            items += f"{desc}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
