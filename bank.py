# Includes all the information and etc.
from transaction import Transaction

class Bank:
    
    def __init__(self):
        self.wallet = []

    # Add 
    def add_transaction(self, transaction):
        self.wallet.append(transaction)

    # Remove
    def delete_transaction(self, title):
        for occur in self.wallet:
            if occur.title == title:
                self.wallet.remove(occur)
                return f"{title} has been removed."
            return f"{title} is not found."

    # Display all
    def display_information(self):
        
    # Search

    # Save 

    # Load