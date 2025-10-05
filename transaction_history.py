from utils import find_account

def transaction_history(accounts, name, pin):
    acc = find_account(accounts, name, pin)
    if acc:
        print(f"📜 Transaction History for {acc['name']}:")
        if acc["transactions"]:
            for t in acc["transactions"]:
                print("-", t)
        else:
            print("No transactions yet.")
    else:
        print("❌ Invalid name or PIN")
