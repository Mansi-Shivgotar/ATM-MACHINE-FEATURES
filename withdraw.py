from utils import find_account

def withdraw(accounts, name, pin, amount):
    acc = find_account(accounts, name, pin)
    if acc:
        if acc["balance"] >= amount:
            acc["balance"] -= amount
            acc["transactions"].append(f"Withdrew ₹{amount}")
            print(f"✅ ₹{amount} withdrawn successfully. New Balance: ₹{acc['balance']}")
        else:
            print("❌ Insufficient Balance")
    else:
        print("❌ Invalid name or PIN")
