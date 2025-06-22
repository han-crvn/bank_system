# Includes all the information and etc.

# Import transaction and json.
from transaction import Transaction, RecurringTransaction
import json

class Bank:
    
    # Initialize empty list.
    def __init__(self):
        self.wallet = []

    # Add transaction.
    def add_transaction(self, transaction):
        self.wallet.append(transaction)

    # Remove transaction.
    def delete_transaction(self, title):
        for occur in self.wallet:
            if occur.title == title:
                self.wallet.remove(occur)
                return f"{title} has been removed."
            return f"{title} is not found."

    # Display all information.
    def display_information(self):
        if not self.wallet:
            return "No transaction has been made in your bank."
        return "\n".join([transaction.display_info() for transaction in self.wallet])

    # Search certain transaction.
    def search_wallet(self, query):
        found = [trans for trans in self.wallet if query.lower() in trans.title.lower() or query.lower() in trans.type.lower()]
        if not found:
            return "No transaction has been made."
        return "\n".join([transaction.display_info() for transaction in found])
    
    # Save transaction.
    def save_information(self, file_name = "wallet.json"):
        data = [{"class": transaction.__class__.__name__, "title": transaction.title, "amount": transaction.amount, "type": transaction.type, "note": transaction.note } for transaction in self.wallet]
        with open(file_name, "a") as file:
            json.dump(data, file, indent = 4)


    # Load transaction.
    def load_bank(self, file_name="wallet.json"):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                self.wallet = []
                for trans in data:
                    if trans.get("class") == "RecurringTransaction":
                        info = RecurringTransaction(trans["title"], trans["amount"], trans["type"], trans["frequency"], trans.get("note", ""))
                    else:
                        info = Transaction(trans["title"], trans["amount"], trans["type"], trans.get("note", ""))
                    self.wallet.append(info)
        except FileNotFoundError:
            print("The file does not exist.")