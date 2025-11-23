# API Reference

This document describes each component of the **Budget App**.

---

## 🧱 Category Class

### **Constructor**
```python
Category(name: str)
```
Creates a new budget category.

---

### **Methods**

#### `deposit(amount, description="")`
Add money to the ledger.

#### `withdraw(amount, description="")`
Subtract money from the ledger if funds are available.

Returns:
- `True` on success  
- `False` if insufficient funds  

#### `transfer(amount, category)`
Moves money from one category to another.

#### `get_balance()`
Returns the current total balance.

#### `check_funds(amount)`
Returns `True` if the amount can be withdrawn; otherwise `False`.

#### `__str__()`
Returns a formatted ledger display, including category name, entries, and total.

---

## 📊 Function: `create_spend_chart(categories)`

Generates a vertical bar chart showing percentage spending per category.

Arguments:
- `categories` — list of `Category` objects

Returns a formatted multi-line string ready for printing.
