from budget_app.core import Category
from budget_app.chart import create_spend_chart

def test_spend_chart_output():
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")

    food.deposit(1000)
    food.withdraw(150)

    clothing.deposit(500)
    clothing.withdraw(50)

    auto.deposit(1000)
    auto.withdraw(100)

    chart = create_spend_chart([food, clothing, auto])

    assert "Percentage spent by category" in chart

    # Category names appear vertically — test by characters, not whole names
    for char in "Food":
        assert char in chart

    for char in "Clothing":
        assert char in chart

    for char in "Auto":
        assert char in chart
