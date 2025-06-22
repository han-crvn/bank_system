# Includes all the transaction that are availables.

class Transaction:
    
    # Initialize necessarry variables.
    def __init__(self, title, amount, type, note = ""):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note
    
    # Display information.
    def display_info(self):
        return f"Transaction:\n Expense: {self.title}\n Amount: {self.amount}\n Type: {self.type}\n Note: {self.note}"