# Command Line Interface (CLI)

The Budget App includes a simple CLI that can generate spending charts directly from the terminal.

---

## ▶️ Running the CLI

Use the module execution syntax:

```bash
python -m budget_app --chart Food Clothing Entertainment
```

This command will generate a spend chart for the listed categories.

---

## ⚙️ Arguments

| Flag | Description |
|------|-------------|
| `--chart` | Generates a spend chart with the provided category names |

---

## 📝 Example

```bash
python -m budget_app --chart Food Clothing Auto
```

This will output a vertical bar chart showing spending (placeholder values if no ledger entries exist yet).

---

## ❗ Note

The CLI currently creates empty categories using the names provided.  
To produce charts based on real spending data, use the Python API to populate ledgers in a script.
