from check_balance import check_balance
from deposit import deposit
from withdraw import withdraw
from transaction_history import transaction_history

def menu(accounts):
    while True:
        print("\n===== ATM Machine =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "5":
            print("👋 Thank you for using the ATM. Goodbye!")
            break

        name = input("Enter Name: ")
        try:
            pin = int(input("Enter PIN: "))
        except:
            print("❌ PIN must be numbers only.")
            continue

        if choice == "1":
            check_balance(accounts, name, pin)
        elif choice == "2":
            try:
                amount = int(input("Enter amount to deposit: "))
                deposit(accounts, name, pin, amount)
            except:
                print("❌ Invalid amount")
        elif choice == "3":
            try:
                amount = int(input("Enter amount to withdraw: "))
                withdraw(accounts, name, pin, amount)
            except:
                print("❌ Invalid amount")
        elif choice == "4":
            transaction_history(accounts, name, pin)
        else:
            print("❌ Invalid choice. Please try again.")
