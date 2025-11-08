# Task 2: Sum of Integers from 1 to 50 Using a Loop

def main():
    print("=== Sum of Integers from 1 to 50 ===")

    total = 0
    for i in range(1, 51):
        total += i

    print(f"The sum of integers from 1 to 50 is: {total}")

if __name__ == "__main__":
    main()
