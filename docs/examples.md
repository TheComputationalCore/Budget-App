
---

# 📄 `docs/examples.md`
```markdown
# Examples

Here are practical examples demonstrating full usage of the **Budget App**.

---

## Full Workflow

```python
from budget_app import Category, create_spend_chart

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial funds")
food.withdraw(15.89, "groceries")
food.withdraw(10.15, "snacks")

clothing.deposit(500)
clothing.withdraw(25.55, "shirt")

auto.deposit(1000)
auto.withdraw(100, "repair")

print(food)
print(create_spend_chart([food, clothing, auto]))
