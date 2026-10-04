import pytest
from app.bank_app import BankAccount


def test_initial_balance():
    account = BankAccount("Gagan", 1000)
    assert account.get_balance() == 1000


def test_deposit_success():
    account = BankAccount("Gagan", 500)
    account.deposit(500)
    account.get_balance() == 1000


def test_withdraw_success():
    account = BankAccount("Gagan", 1000)
    account.withdraw(300)
    assert account.get_balance() == 700


def test_withdraw_more_than_balance():
    account = BankAccount("Gagan", 200)
    with pytest.raises(ValueError):
        account.withdraw(500)
