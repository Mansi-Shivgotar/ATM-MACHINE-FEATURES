from utils import find_account

def check_balance(accounts, name, pin):
    acc = find_account(accounts, name, pin)
    if acc:
        print(f"✅ Balance for {acc['name']}: ₹{acc['balance']}")
    else:
        print("❌ Invalid name or PIN")
