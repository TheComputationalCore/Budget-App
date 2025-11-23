# Contributing to Budget App

Thank you for your interest in contributing!  
This document outlines the guidelines and workflow for contributing to the project.

---

## 🧱 How to Contribute

### 1. Fork the Repository
Click **Fork** in the top-right corner of GitHub.

### 2. Clone Your Fork
```bash
git clone https://github.com/<your-username>/Budget-App.git
cd Budget-App
```

### 3. Create a Feature Branch
```bash
git checkout -b feature-name
```

### 4. Install the Project
```bash
pip install -e .
```

### 5. Run Tests
```bash
pytest -q
```

### 6. Make Your Changes
Follow the existing formatting and naming conventions.

### 7. Commit Your Work
```bash
git commit -m "Describe your feature or fix"
```

### 8. Push and Open a PR
```bash
git push origin feature-name
```

Then open a **Pull Request** on GitHub.

---

## 🔍 Code Style
We use:

- **Black** for formatting  
- **Flake8** for linting  

These run automatically in GitHub Actions.

---

## 🧪 Tests
Please ensure all tests pass before submitting a PR.

If you add new features, add tests under:

```
tests/
```

---

## 💬 Questions?
Open an issue on GitHub.
