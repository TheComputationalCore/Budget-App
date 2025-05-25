class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": float(amount), "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -float(amount), "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append({"amount": -float(amount), 
                              "description": f"Transfer to {category.name}"})
            category.ledger.append({"amount": float(amount), 
                                 "description": f"Transfer from {self.name}"})
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

def create_spend_chart(categories):
    # Calculate total spent and spending per category
    spent_by_category = []
    total_spent = 0
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_by_category.append(spent)
        total_spent += spent
    
    # Calculate percentages rounded down to nearest 10
    percentages = []
    for spent in spent_by_category:
        if total_spent > 0:
            percentage = (spent / total_spent * 100) // 10 * 10
        else:
            percentage = 0
        percentages.append(int(percentage))

    # Create chart
    chart = "Percentage spent by category\n"
    
    # Add percentage lines
    for i in range(100, -10, -10):
        line = f"{str(i).rjust(3)}| "
        for percentage in percentages:
            line += "o  " if percentage >= i else "   "
        # No extra space at the end
        chart += line + "\n"
    
    # Add horizontal line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
    
    # Add category names vertically
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        line = "     "  # 5 spaces to align with bars
        for category in categories:
            char = category.name[i] if i < len(category.name) else ' '
            line += f"{char}  "
        # No extra space at the end
        chart += line + "\n"
    
    # Remove trailing newline
    return chart.rstrip("\n")