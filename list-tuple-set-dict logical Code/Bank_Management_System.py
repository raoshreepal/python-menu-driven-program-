# Bank Management System

accounts = {}

def create_account():
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))
    accounts[acc_no] = {"name": name, "balance": balance}
    print("Account created.")

def view_accounts():
    if not accounts:
        print("No accounts available.")
        return
    for acc_no, details in accounts.items():
        print(f"Account: {acc_no}, Name: {details['name']}, Balance: {details['balance']}")

def deposit():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_no]["balance"] += amount
        print("Deposit successful.")
    else:
        print("Account not found.")

def withdraw():
    acc_no = input("Enter account number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[acc_no]["balance"]:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")

def search_account():
    acc_no = input("Enter account number to search: ")
    if acc_no in accounts:
        print("Account found:", accounts[acc_no])
    else:
        print("Account not found.")


while True:
    print("\n--- Bank Management ---")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Search Account")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        view_accounts()
    elif choice == '3':
        deposit()
    elif choice == '4':
        withdraw()
    elif choice == '5':
        search_account()
    elif choice == '6':
        break
    else:
        print("Invalid choice!")


