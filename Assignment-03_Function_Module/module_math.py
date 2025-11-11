import math

def main():
    print("---- Math Operations Program ----")
    try:
        num = float(input("Enter a number: "))

        # Square root
        if num >= 0:
            square_root = math.sqrt(num)
        else:
            square_root = "Undefined for negative numbers"

        # Natural log (ln)
        if num > 0:
            natural_log = math.log(num)  # ln(num)
        else:
            natural_log = "Undefined for zero or negative numbers"

        # Sine (in radians)
        sine_value = math.sin(num)

        # Display results
        print("\nResults:")
        print(f"Square root of {num}: {square_root}")
        print(f"Natural log (ln) of {num}: {natural_log}")
        print(f"Sine of {num} radians: {sine_value}")

    except ValueError:
        print("Invalid input. Please enter a valid number (e.g. 3, 4.5, -2).")

if __name__ == "__main__":
    main()
