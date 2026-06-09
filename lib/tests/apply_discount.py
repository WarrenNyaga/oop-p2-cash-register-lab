def apply_discount(self):
        """Applies the discount percentage factor and pops the last transaction."""
        # Guard clause check: verify if any transactions are present
        if not self.previous_transactions:
            print("There is no discount to apply(void_last_transaction).")
            return

        # Apply percentage calculation to decrease total
        # Example: 20% discount means total becomes total * 0.80
        self.total *= (1 - (self.discount / 100))

        # Remove the last transaction record from the history log
        last_transaction = self.previous_transactions.pop()

        # Keep items list in sync by removing the name of the popped item
        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])