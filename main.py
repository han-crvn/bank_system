# This part includes the options and in this part we can run the program.

# Import the bank and transaction file.
from bank import Bank
from transaction import Transaction, RecurringTransaction

def main():

    # Call the bank.py
    wallet = Bank()

    while True:
        try:

            # Print the menu.
            print("\n===== Personal Bank System =====")
            print("1. Add Single Transaction")
            print("2. Add Non-Single Transaction")
            print("3. Remove a Transaction")
            print("4. Display All Transaction")
            print("5. Search for a Transaction")
            print("6. Save a Transaction")
            print("7. Load Transaction from file")
            print("8. Exit Program")
            
            # Allow users to choose from menu.
            choice = input("\nEnter your choice (1-7): ")
            
            # If user choose this option, allow them to add single transaction.
            if choice == "1":

                # Input title.
                title = input("\nEnter the title: ")
                
                try:
                    # Input amount.
                    amount = float(input("\nEnter amount: "))
                
                # Catch invalid input.
                except ValueError:
                    print("\nInvalid amount entered.")
                    continue
                
                # Input type.
                type = input("\nEnter Type: ")
                
                # Add note.
                note = input("\nEnter a note (optional): ")

                # Save the transaction.
                action = Transaction(title, amount, type, note)
                wallet.add_transaction(action)
                print("\nThe transaction has been saved to the program.")

           # If user choose this option, allow them to add non-single transaction.
            elif choice == "2":
                
                # Input title.
                title = input("\nEnter the title: ")
                
                try:
                    # Input amount.
                    amount = float(input("\nEnter amount: "))
                
                # Catch invalid input.
                except ValueError:
                    print("\nInvalid amount entered.")
                    continue
                
                # Input type.
                type = input("\nEnter Type: ")

                # Input frequency.
                frequency = input("\nEnter the frequency (Yearly, Monthly, Weekly): ")
                
                # Add note.
                note = input("\nEnter a note (optional): ")
                
                 # Save the transaction.
                recurring = RecurringTransaction(title, amount, type, frequency, note)
                wallet.add_transaction(recurring)
                print("\nThe transaction has been saved to the program.")

            # If user choose this option, allow them to delete certain transaction.
            elif choice == "3":
                
                # Input title.
                title = input("\nEnter the title: ")

                # Display result.
                print(wallet.delete_transaction(title))

            # If user choose this option, show informations.
            elif choice == "4":
                print(wallet.display_information())

            # If user choose this option, allow user to search transactions.
            elif choice == "5":
                
                # Input title.
                query = input("\nEnter the title: ")

                # Display result.
                print(wallet.search_wallet(query))

            # If user choose this option, save information.
            elif choice == "6":
                wallet.save_information()
                print("\nSuccessfully saved!")

            # If user choose this option, load information.
            elif choice == "7":
                wallet.load_bank()
                print("\nLoaded json file.")

            # If user choose this option, exit program.
            elif choice == "8":
                print("\nLeaving the program.")
                break
            
            # Catch invalid input.
            else:
                print("\nInvalid input. Please try again.")

        # Catch invalid input.
        except ValueError:
            print("\nnvalid input. Please try again.")

# Run the program.
if __name__ == "__main__":
    main()