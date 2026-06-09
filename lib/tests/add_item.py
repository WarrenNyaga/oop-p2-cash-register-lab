def add_item(self, item, price, quantity):
        """Adds product details to the current instance cart."""
        # Update the overall running total
        self.total += price * quantity
        
        # Track the name of the item
        self.items.append(item)
        
        # Build the structured dictionary log entry
        transaction_entry = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction_entry)