def main():
    balance = 0.0
    print("=" * 40)
    print("       WELCOME TO THE MOCKUP ATM       ")
    print("=" * 40)

    while True:
        print("\nMAIN MENU")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Balance Enquiry")
        print("4. Exit")
        print("-" * 40)

        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("[Error] Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            print("\n>>> DEPOSIT TRANSACTION <<<")
            try:
                amount = float(input("Enter deposit amount (INR): ").strip())
                if amount <= 0:
                    print("[Error] Deposit amount must be greater than zero.")
                    continue
            except ValueError:
                print("[Error] Invalid input. Please enter a valid numeric value.")
                continue

            balance += amount
            print(f"[Success] Deposited: INR {amount:,.2f}")
            print(f"Current Balance: INR {balance:,.2f}")

        elif choice == 2:
            print("\n>>> WITHDRAWAL TRANSACTION <<<")
            try:
                amount = float(input("Enter withdrawal amount (INR): ").strip())
                if amount <= 0:
                    print("[Error] Withdrawal amount must be greater than zero.")
                    continue
            except ValueError:
                print("[Error] Invalid input. Please enter a valid numeric value.")
                continue

            if amount > balance:
                print("[Denied] Insufficient balance for this transaction.")
                print(f"Available Balance: INR {balance:,.2f}")
            else:
                balance -= amount
                print(f"[Success] Withdrawn: INR {amount:,.2f}")
                print(f"Remaining Balance: INR {balance:,.2f}")

        elif choice == 3:
            print("\n>>> BALANCE ENQUIRY <<<")
            print(f"Your total available balance is: INR {balance:,.2f}")

        elif choice == 4:
            print("\n" + "=" * 40)
            print(" Thank you for using our ATM. Goodbye! ")
            print("=" * 40)
            break

        else:
            print("[Error] Invalid Choice. Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()
