def create_spend_chart(categories):
    """Generate a vertical bar chart showing spending percentages."""

    spent_by_category = []
    total_spent = 0

    # Calculate money spent per category
    for category in categories:
        spent = sum(
            -item["amount"] for item in category.ledger if item["amount"] < 0
        )
        spent_by_category.append(spent)
        total_spent += spent

    # Convert to percentage buckets (10% steps)
    percentages = [
        int(((spent / total_spent) * 100) // 10 * 10) if total_spent else 0
        for spent in spent_by_category
    ]

    chart = "Percentage spent by category\n"

    # Percentage rows
    for i in range(100, -10, -10):
        row = f"{str(i).rjust(3)}| "
        for p in percentages:
            row += "o  " if p >= i else "   "
        chart += row + "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        row = "     "
        for c in categories:
            row += (c.name[i] if i < len(c.name) else " ") + "  "
        chart += row + "\n"

    return chart.rstrip()
