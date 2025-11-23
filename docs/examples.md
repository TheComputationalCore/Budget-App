# Examples

This page contains complete examples demonstrating full usage of the **Budget App**.

---

## 📘 Full Workflow Example

```python
from budget_app import Category, create_spend_chart

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(15.89, "groceries")
food.withdraw(10.15, "snacks")

clothing.deposit(500)
clothing.withdraw(25.55, "shirt")

auto.deposit(1000)
auto.withdraw(100, "repair")

print(food)
print(create_spend_chart([food, clothing, auto]))
```

---

## 📊 Sample Spend Chart Output

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|          
 50|    o     
 40|    o     
 30|    o     
 20| o  o     
 10| o  o     
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

---

## 🧾 Sample Ledger Output

```
*************Food*************
initial deposit        1000.00
groceries               -15.89
snacks                  -10.15
Transfer to Clothing    -50.00
Total: 923.96
```

---

Continue exploring the documentation via the sidebar.
