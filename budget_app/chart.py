def create_spend_chart(categories):
    spent_by_category = []
    total_spent = 0

    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_by_category.append(spent)
        total_spent += spent

    percentages = []
    for spent in spent_by_category:
        if total_spent > 0:
            percentage = (spent / total_spent * 100) // 10 * 10
        else:
            percentage = 0
        percentages.append(int(percentage))

    chart = "Percentage spent by category\n"

    for i in range(100, -10, -10):
        line = f"{str(i).rjust(3)}| "
        for percentage in percentages:
            line += "o  " if percentage >= i else "   "
        chart += line + "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        line = "     "
        for category in categories:
            char = category.name[i] if i < len(category.name) else " "
            line += f"{char}  "
        chart += line + "\n"

    return chart.rstrip("\n")
