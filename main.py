# This part includes the options and in this part we can run the program.
from bank import Bank
from transaction import Transaction


def main():
    wallet = Bank()
    while True:
        try:
            print("\n===== Personal Bank System =====")
            print("1. Add a Transaction")
            print("2. Remove a Transaction")
            print("3. Display All Transaction")
            print("4. Search for a Transaction")
            print("5. Save a Transaction")
            print("6. Load Transaction from file")
            print("7. Exit Program")

            choice = input("\nEnter your choice (1-7): ")

            if choice == "1":
                title = input("\nEnter the title: ")
                
                try:
                    amount = float(input("\nEnter amount: "))
                except ValueError:
                    print("\nInvalid amount entered.")
                    continue

                type = input("\nExpense or Deposit: ")
                action = Transaction(title, amount, type)
                wallet.add_transaction(action)

            elif choice == "2":
                title = input("\nEnter the title: ")
                print(wallet.delete_transaction(title))

            elif choice == "3":
                print(wallet.display_information())

            elif choice == "4":
                query = input("\nEnter the title: ")
                print(wallet.search_wallet(query))

            elif choice == "5":
                wallet.save_information()
                print("\nSuccessfully saved!")

            elif choice == "6":
                wallet.load_bank()
                print("\nLoaded json file.")

            elif choice == "7":
                print("\nLeaving the program.")
                break

            else:
                print("\nInvalid input. Please try again.")

        except ValueError:
            print("\nnvalid input. Please try again.")

if __name__ == "__main__":
    main()