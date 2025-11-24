# 📊 Budget App

A clean, Pythonic toolkit for managing personal budget categories, tracking transactions, and visualizing spending through percentage-based charts.  
Fully documented, fully tested, and shipped with a simple command-line interface.

## 🔖 Badges

![Tests](https://img.shields.io/github/actions/workflow/status/TheComputationalCore/Budget-App/tests.yml?label=Tests&logo=pytest)
![Docs](https://img.shields.io/github/actions/workflow/status/TheComputationalCore/Budget-App/deploy-docs.yml?label=Docs&logo=mkdocs)
![Deployed](https://img.shields.io/badge/Deployed-GitHub%20Pages-brightgreen?logo=github)
![License](https://img.shields.io/badge/License-MIT-blue)

## 🚀 Features

- Track deposits, withdrawals, and transfers  
- Maintain multiple independent budget categories  
- Validate funds before spending or transferring  
- Generate clean text-based spending charts  
- Command-line interface included  
- Full MkDocs documentation  
- Pytest test suite  
- Automatic Black/Flake8 linting  

## 📦 Installation

```bash
git clone https://github.com/TheComputationalCore/Budget-App.git
cd Budget-App
pip install .
```

## 🧱 Usage (Python API)

```python
from budget_app import Category, create_spend_chart

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(15.89, "groceries")

print(food)
print(create_spend_chart([food, clothing, auto]))
```

## 🖥️ Command Line Interface

Generate a spend chart from the terminal:

```bash
python -m budget_app --chart Food Clothing Auto
```

| Flag      | Description                                    |
|-----------|------------------------------------------------|
| `--chart` | Generate a spending chart for given categories |

## 📊 Sample Spend Chart

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

## 🧾 Sample Ledger Output

```
*************Food*************
initial deposit        1000.00
groceries               -15.89
snacks                  -10.15
Transfer to Clothing    -50.00
Total: 923.96
```

## 📚 Documentation

Full documentation is available here:  
👉 **https://thecomputationalcore.github.io/Budget-App/**

## 📂 Project Structure

```
budget_app/
    __init__.py
    core.py
    chart.py
    cli.py
docs/
    api.md
    cli.md
    examples.md
    usage.md
tests/
    test_core.py
    test_chart.py
.github/workflows/
    tests.yml
    lint.yml
    deploy-docs.yml
```

## 🧪 Running Tests

```bash
pytest -q
```

## 🤝 Contributing

See **CONTRIBUTING.md** for complete workflow.

## 🔐 Security

For reporting vulnerabilities, see **SECURITY.md**.

## 📄 License

MIT License  
Made with ❤️ by **The Computational Core**
