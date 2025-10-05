from utils import find_account

def deposit(accounts, name, pin, amount):
    acc = find_account(accounts, name, pin)
    if acc:
        acc["balance"] += amount
        acc["transactions"].append(f"Deposited ₹{amount}")
        print(f"✅ ₹{amount} deposited successfully. New Balance: ₹{acc['balance']}")
    else:
        print("❌ Invalid name or PIN")
