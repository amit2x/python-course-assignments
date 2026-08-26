from datetime import datetime

# Create a reusable header to show for each function with passing title as a parameter
def print_header(title):
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

# Add transaction history with four parameter , where we have used transactions as a list datatype not tuple.
def add_transaction(transactions, transaction_type, amount, balance):
    transactions.append({
        "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "type": transaction_type,
        "amount": amount,
        "balance": balance
    })

# Perform Deposit money transaction.
def deposit_money(balance, transactions):
    while True:
        print_header("DEPOSIT TRANSACTION")

        try:
            amount = float(input("Enter deposit amount (INR): ").strip())

            if amount <= 0:
                print("[Error] Deposit amount must be greater than zero.")
                continue

        except ValueError:
            print("[Error] Please enter a valid numeric amount.")
            continue

        balance += amount

        # Log Transaction to show transaction history
        add_transaction(
            transactions,
            "DEPOSIT",
            amount,
            balance
        )

        print(f"\n[Success] Deposited: INR {amount:,.2f}")
        print(f"Current Balance: INR {balance:,.2f}")

        print("\nWhat would you like to do?")
        print("1. Deposit More Money")
        print("2. Return to Main Menu")
        print("3. Exit ATM")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            continue
        elif choice == "2":
            return balance, False
        elif choice == "3":
            return balance, True
        else:
            print("[Error] Invalid choice. Returning to Main Menu.")
            return balance, False

# perform withdraw transaction
def withdraw_money(balance, transactions):
    while True:
        print_header("WITHDRAWAL TRANSACTION")

        try:
            amount = float(input("Enter withdrawal amount (INR): ").strip())

            if amount <= 0:
                print("[Error] Withdrawal amount must be greater than zero.")
                continue

        except ValueError:
            print("[Error] Please enter a valid numeric amount.")
            continue

        if amount > balance:
            print("\n[Denied] Insufficient balance.")
            print(f"Available Balance: INR {balance:,.2f}")

            print("\nWhat would you like to do?")
            print("1. Try Another Amount")
            print("2. Return to Main Menu")
            print("3. Exit ATM")

            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                continue
            elif choice == "2":
                return balance, False
            elif choice == "3":
                return balance, True
            else:
                print("[Error] Invalid choice. Returning to Main Menu.")
                return balance, False

        balance -= amount

        # Log transaction history
        add_transaction(
            transactions,
            "WITHDRAW",
            amount,
            balance
        )

        print(f"\n[Success] Withdrawn: INR {amount:,.2f}")
        print(f"Remaining Balance: INR {balance:,.2f}")

        print("\nWhat would you like to do?")
        print("1. Withdraw More Money")
        print("2. Return to Main Menu")
        print("3. Exit ATM")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            continue
        elif choice == "2":
            return balance, False
        elif choice == "3":
            return balance, True
        else:
            print("[Error] Invalid choice. Returning to Main Menu.")
            return balance, False

# perform Balance enquiry
def balance_enquiry(balance):
    print_header("BALANCE ENQUIRY")

    print(f"Available Balance : INR {balance:,.2f}")

    input("\nPress Enter to return to Main Menu...")


# Perform Mini_statement
def mini_statement(transactions, balance):
    print_header("MINI STATEMENT")
    # check list is empty or not
    if not transactions:
        print("No transactions available.")
        print(f"\nCurrent Balance: INR {balance:,.2f}")
        input("\nPress Enter to return to Main Menu...")
        return

    print(
        f"{'Date & Time':<20}"
        f"{'Type':<12}"
        f"{'Amount':>15}"
        f"{'Balance':>15}"
    )

    print("-" * 62)

    # Show last 5 transactions
    recent_transactions = transactions[-5:]

    for transaction in recent_transactions:
        print(
            f"{transaction['date']:<20}"
            f"{transaction['type']:<12}"
            f"INR {transaction['amount']:>10,.2f}"
            f"INR {transaction['balance']:>10,.2f}"
        )

    print("-" * 62)
    print(f"Current Balance: INR {balance:,.2f}")

    input("\nPress Enter to return to Main Menu...")

# show transaction history
def transaction_history(transactions):
    print_header("TRANSACTION HISTORY")

    if not transactions:
        print("No transactions have been performed yet.")
        input("\nPress Enter to return to Main Menu...")
        return

    for index, transaction in enumerate(transactions, start=1):
        print(
            f"{index}. "
            f"{transaction['date']} | "
            f"{transaction['type']} | "
            f"INR {transaction['amount']:,.2f} | "
            f"Balance: INR {transaction['balance']:,.2f}"
        )

    input("\nPress Enter to return to Main Menu...")

# mock transfer money
def transfer_money(balance, transactions):
    print_header("MONEY TRANSFER")

    account = input("Enter beneficiary account number: ").strip()

    if not account.isdigit():
        print("[Error] Invalid account number.")
        input("\nPress Enter to return to Main Menu...")
        return balance, False

    if len(account) < 6:
        print("[Error] Account number must contain at least 6 digits.")
        input("\nPress Enter to return to Main Menu...")
        return balance, False

    try:
        amount = float(input("Enter transfer amount (INR): ").strip())

        if amount <= 0:
            print("[Error] Transfer amount must be greater than zero.")
            input("\nPress Enter to return to Main Menu...")
            return balance, False

    except ValueError:
        print("[Error] Invalid amount.")
        input("\nPress Enter to return to Main Menu...")
        return balance, False

    if amount > balance:
        print("[Denied] Insufficient balance.")
        input("\nPress Enter to return to Main Menu...")
        return balance, False

    print("\nTransfer Details")
    print("-" * 40)
    print(f"Beneficiary Account : XXXX{account[-4:]}")
    print(f"Transfer Amount     : INR {amount:,.2f}")

    confirm = input("\nConfirm transfer? (Y/N): ").strip().lower()

    if confirm != "y":
        print("[Cancelled] Transfer cancelled.")
        input("\nPress Enter to return to Main Menu...")
        return balance, False

    balance -= amount

    add_transaction(
        transactions,
        "TRANSFER",
        amount,
        balance
    )

    print("\n[Success] Money transferred successfully.")
    print(f"Transferred Amount : INR {amount:,.2f}")
    print(f"Remaining Balance  : INR {balance:,.2f}")

    input("\nPress Enter to return to Main Menu...")

    return balance, False

# change pin mockup
def change_pin(current_pin):
    print_header("CHANGE PIN")

    entered_pin = input("Enter current PIN: ").strip()

    if entered_pin != current_pin:
        print("[Error] Incorrect current PIN.")
        input("\nPress Enter to return to Main Menu...")
        return current_pin

    new_pin = input("Enter new 4-digit PIN: ").strip()

    if not new_pin.isdigit() or len(new_pin) != 4:
        print("[Error] PIN must contain exactly 4 digits.")
        input("\nPress Enter to return to Main Menu...")
        return current_pin

    confirm_pin = input("Confirm new PIN: ").strip()

    if new_pin != confirm_pin:
        print("[Error] PIN confirmation does not match.")
        input("\nPress Enter to return to Main Menu...")
        return current_pin

    print("[Success] PIN changed successfully.")

    input("\nPress Enter to return to Main Menu...")

    return new_pin


def main():

    balance = 0.0
    # Default Pin to start ATM
    current_pin = "1234"

    # For storing transactions history, choosen datatype is list
    transactions = []

    print("=" * 50)
    print("         WELCOME TO THE MOCKUP ATM")
    print("=" * 50)

    # Simple PIN authentication with attempts limit
    attempts = 3

    while attempts > 0:

        pin = input("\nEnter your 4-digit PIN: ").strip()

        if pin == current_pin:
            print("[Success] Login successful.")
            break

        attempts -= 1

        if attempts > 0:
            print(f"[Error] Incorrect PIN. Attempts remaining: {attempts}")
        else:
            print("[Blocked] Too many incorrect attempts.")
            return

    while True:

        print("\n")
        print("=" * 50)
        print("                 MAIN MENU")
        print("=" * 50)

        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Balance Enquiry")
        print("4. Mini Statement")
        print("5. Transaction History")
        print("6. Transfer Money")
        print("7. Change PIN")
        print("8. Exit")

        print("-" * 50)

        try:
            choice = int(
                input("Enter your choice (1-8): ").strip()
            )

        except ValueError:
            print(
                "[Error] Invalid input. "
                "Please enter a number between 1 and 8."
            )
            continue

        # Calling defined function with passing parameter based on entered choice.
        if choice == 1:

            balance, exit_atm = deposit_money(
                balance,
                transactions
            )

            if exit_atm:
                break

        elif choice == 2:

            balance, exit_atm = withdraw_money(
                balance,
                transactions
            )

            if exit_atm:
                break

        elif choice == 3:

            balance_enquiry(balance)

        elif choice == 4:

            mini_statement(
                transactions,
                balance
            )

        elif choice == 5:

            transaction_history(
                transactions
            )

        elif choice == 6:

            balance, exit_atm = transfer_money(
                balance,
                transactions
            )

            if exit_atm:
                break

        elif choice == 7:

            current_pin = change_pin(
                current_pin
            )

        elif choice == 8:

            break

        else:

            print(
                "[Error] Invalid Choice. "
                "Please select an option between 1 and 8."
            )

    print("\n" + "=" * 50)
    print("       Thank you for using our ATM.")
    print("              Goodbye!")
    print("=" * 50)


if __name__ == "__main__":
    main()