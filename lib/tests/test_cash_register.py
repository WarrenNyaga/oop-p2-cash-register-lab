import pytest

from lib.cash_register import CashRegister


def test_add_item():
	cr = CashRegister()
	cr.add_item("apple", 10, 2)
	assert cr.total == 20
	assert cr.items == ["apple", "apple"]
	assert cr.previous_transactions[-1] == {"item": "apple", "price": 10, "quantity": 2}


def test_apply_discount_no_transactions(capsys):
	cr = CashRegister(20)
	cr.apply_discount()
	captured = capsys.readouterr()
	assert "There is no discount to apply." in captured.out


def test_apply_discount_with_transaction():
	cr = CashRegister(20)
	cr.add_item("shirt", 100, 1)
	cr.apply_discount()
	assert pytest.approx(cr.total, rel=1e-3) == 80
	assert cr.previous_transactions == []
	assert cr.items == []


def test_void_last_transaction_no_transactions(capsys):
	cr = CashRegister()
	cr.void_last_transaction()
	captured = capsys.readouterr()
	assert "There is no transaction to void." in captured.out


def test_void_last_transaction():
	cr = CashRegister()
	cr.add_item("book", 15, 2)
	cr.void_last_transaction()
	assert cr.total == 0
	assert cr.items == []
	assert cr.previous_transactions == []


def test_invalid_discount_sets_zero(capsys):
	cr = CashRegister(discount="bad")
	captured = capsys.readouterr()
	assert "Not valid discount" in captured.out
	assert cr.discount == 0
