# Includes all the information and etc.
from transaction import Transaction
import json

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
        if not self.wallet:
            return f"No transaction has been made in your bank."
        return f"\n".join([Transaction.display_info() for transaction in self.wallet])
    
    # Search
    def search_wallet(self, query):
        found = [trans for trans in self.wallet if query.lower() in trans.title.lower() or query.lower() in trans.type.lower()]
        if not found:
            return f"No transaction has been made."
        return "\n".join([Transaction.display_info() for transaction in found])
    
    # Save 
    def save_information(self, file_name = "wallet.json"):
        data = [{"Expense": Transaction.title, "Amount": Transaction.amount, "Type:": Transaction.type, "Note:": Transaction.note} for transaction in self.wallet]
        with open(file_name, "w") as file:
            json.dump(data, file)

    # Load
    def load_bank(self, file_name = "wallet.json"):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                self.wallet = [Transaction(trans["title"], trans["amount"], trans["type"], trans["note"]) for trans in data]
        except FileNotFoundError:
            print("The file does not exist.")