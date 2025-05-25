# Budget App

A Python project to manage budget categories and visualize spending as a bar chart.

## Overview

This project implements a `Category` class for tracking financial transactions (deposits, withdrawals, transfers) and a `create_spend_chart` function to generate a bar chart of spending percentages across categories. It supports precise formatting for ledger display and spending visualization.

## Features

- **Category Management**:
  - Initialize categories (e.g., Food, Clothing) with a ledger to track transactions.
  - Deposit funds with optional descriptions (defaults to empty string).
  - Withdraw funds (as negative amounts) if sufficient balance exists.
  - Transfer funds between categories with descriptive entries.
  - Check available funds before withdrawals or transfers.
  - Display ledger with formatted descriptions (first 23 characters), amounts (7 characters, right-aligned, two decimal places), and total balance.
- **Spending Chart**:
  - Generates a bar chart showing percentage spent per category (based on withdrawals only).
  - Percentages rounded down to the nearest 10.
  - Uses 'o' characters for bars, with labels from 0 to 100.
  - Displays category names vertically below bars.
  - Ensures exact spacing and formatting (e.g., two spaces between bars, horizontal line extends two spaces past final bar).
- Supports up to four categories in the spend chart.

## Installation

1. Ensure Python 3.x is installed.
2. Download or clone this repository:
   ```bash
   git clone https://github.com/thesoulseizure/budget-app.git
   ```
3. Navigate to the project directory:
   ```bash
   cd budget-app
   ```

## Usage

1. Save `budget_app.py` in your project directory.
2. Import and use the `Category` class and `create_spend_chart` function in a Python script or interpreter.

Example usage:

```python
# Create categories
food = Category("Food")
clothing = Category("Clothing")

# Add transactions
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.transfer(50, clothing)

# Print category ledger
print(food)

# Create spend chart
print(create_spend_chart([food, clothing]))
```

Output (for `print(food)`):
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Output (for `print(create_spend_chart([food, clothing]))`):
```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|          
 50|          
 40|          
 30|          
 20| o        
 10| o        
  0| o  o     
    ----------
     F  C  
     o  l  
     o  o  
     d  t  
        h  
        i  
        n  
        g
```

## File Structure

- `budget_app.py`: Main Python script containing the `Category` class and `create_spend_chart` function.
- `README.md`: This documentation file.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
