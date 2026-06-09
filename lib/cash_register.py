#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    # route through the setter for validation
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    # Ensure discount is an integer between 0 and 100 inclusive
    if not isinstance(value, int) or not (0 <= value <= 100):
      print("Not valid discount")
      self._discount = 0
    else:
      self._discount = value

  def add_item(self, item, price, quantity=1):
    # Update running total
    self.total += price * quantity

    # Track items (repeat name per quantity)
    for _ in range(quantity):
      self.items.append(item)

    # Log the transaction
    transaction_entry = {"item": item, "price": price, "quantity": quantity}
    self.previous_transactions.append(transaction_entry)

  def apply_discount(self):
    # If no transactions, notify and return
    if not self.previous_transactions:
      print("There is no discount to apply.")
      return

    # Apply discount percentage
    self.total = self.total * (1 - (self.discount / 100))

    # Remove last transaction from history and keep items in sync
    last_transaction = self.previous_transactions.pop()
    for _ in range(last_transaction.get("quantity", 1)):
      if last_transaction["item"] in self.items:
        self.items.remove(last_transaction["item"])

  def void_last_transaction(self):
    if not self.previous_transactions:
      print("There is no transaction to void.")
      return

    last_transaction = self.previous_transactions.pop()

    # Subtract the transaction amount from total
    self.total -= last_transaction["price"] * last_transaction.get("quantity", 1)

    # Remove item names from items list
    for _ in range(last_transaction.get("quantity", 1)):
      if last_transaction["item"] in self.items:
        self.items.remove(last_transaction["item"])
