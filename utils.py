def find_account(accounts, name, pin):
    for acc in accounts:
        if acc["name"].lower() == name.lower() and acc["pin"] == pin:
            return acc
    return None
