def get_number(prompt, allow_float=True):
    while True:
        try:
            s = input(prompt).strip()
            return float(s) if allow_float else int(s)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

def main():
    print("------ Simple Calculator ------")
    while True:
        print("""
            Please choose an option:
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Modulus
            6. Exit
            """)
        try:
            option = int(input("Enter your option (1-6): ").strip())
        except ValueError:
            print("Invalid option. Enter a number between 1 and 6.")
            continue

        if option == 6:
            print("Thank you for using this Calculator, goodbye!")
            break

        if option not in range(1, 6):
            print("Please choose a valid option from 1 to 6.")
            continue

        # For modulus we want integers; for division allow floats
        if option == 5:  # modulus
            num1 = get_number("Enter your first number (integer): ", allow_float=False)
            num2 = get_number("Enter your second number (integer): ", allow_float=False)
        elif option == 4:  # division
            num1 = get_number("Enter your first number: ")
            num2 = get_number("Enter your second number: ")
        else:
            num1 = get_number("Enter your first number: ")
            num2 = get_number("Enter your second number: ")

        # perform operation with safe checks
        try:
            if option == 1:
                result = num1 + num2
                op = "+"
            elif option == 2:
                result = num1 - num2
                op = "-"
            elif option == 3:
                result = num1 * num2
                op = "*"
            elif option == 4:
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                op = "/"
            elif option == 5:
                if num2 == 0:
                    print("Error: Modulus by zero is not allowed.")
                    continue
                result = int(num1) % int(num2)
                op = "%"
            else:
                # should not happen because of previous checks
                print("Unknown option.")
                continue

            # Print result nicely
            print(f"Result: {num1} {op} {num2} = {result}")
        except Exception as e:
            print("An error occurred:", e)

    print("Program ended. Have a nice day!")

if __name__ == "__main__":
    main()
