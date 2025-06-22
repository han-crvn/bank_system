# Includes all the transaction that are availables.

class Transaction:
    
    def __init__(self, title, amount, type, note = ""):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note

    def display_info(self):
        return f"Transaction:\n Expense: {self.title}\n Amount: {self.amount}\n Type: {self.type}\n Note: {self.note}"