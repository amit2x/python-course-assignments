# Task 1: Perform Basic Mathematical Operations

# Take two numbers as input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform basic operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    # Handle division safely
    if num2 != 0:
        division = float(num1 / num2)
    else:
        division = "Undefined (Cannot divide by zero)"

    # Display results
    print("\n--- Results ---")
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
