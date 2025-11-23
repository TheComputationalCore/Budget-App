# Usage Guide

This guide explains how to use the **Budget App** to manage financial categories, track transactions, and generate spending charts.

---

## 🧱 Creating Categories

```python
from budget_app import Category

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")
```

Each category maintains its own ledger.

---

## ➕ Making Deposits

```python
food.deposit(1000, "initial deposit")
clothing.deposit(200)
```

---

## ➖ Making Withdrawals

```python
food.withdraw(15.89, "groceries")
clothing.withdraw(25.55, "shirt purchase")
```

If the withdrawal exceeds available funds:

```python
food.withdraw(99999)   # returns False
```

---

## 🔁 Transferring Funds

```python
food.transfer(50, clothing)
```

Transfers appear in both ledgers:

- From category: `Transfer to Clothing`  
- To category: `Transfer from Food`

---

## 📊 Generating a Spending Chart

```python
from budget_app import create_spend_chart

print(create_spend_chart([food, clothing, auto]))
```

This produces a vertical percentage chart showing how much you've spent in each category.

---

## 📘 Viewing a Category Ledger

```python
print(food)
```

Example output:

```
*************Food*************
initial deposit        1000.00
groceries               -15.89
Transfer to Clothing    -50.00
Total: 934.11
```

---

## 🧭 Next Steps

View:

- [Examples](examples.md)
- [API Reference](api.md)
- [CLI Guide](cli.md)
