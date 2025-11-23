import pytest
from budget_app.core import Category


def test_deposit():
    cat = Category("Food")
    cat.deposit(100, "initial")
    assert cat.get_balance() == 100


def test_withdraw_success():
    cat = Category("Food")
    cat.deposit(200)
    assert cat.withdraw(50, "groceries") is True
    assert cat.get_balance() == 150


def test_withdraw_fail():
    cat = Category("Food")
    cat.deposit(20)
    assert cat.withdraw(100) is False
    assert cat.get_balance() == 20


def test_transfer_success():
    food = Category("Food")
    clothing = Category("Clothing")
    food.deposit(300)
    assert food.transfer(100, clothing) is True
    assert food.get_balance() == 200
    assert clothing.get_balance() == 100


def test_transfer_fail():
    food = Category("Food")
    clothing = Category("Clothing")
    food.deposit(20)
    assert food.transfer(100, clothing) is False
    assert food.get_balance() == 20
    assert clothing.get_balance() == 0
