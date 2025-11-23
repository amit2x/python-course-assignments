"""
Problem Statement:
Write a Python program that:
1. Opens and reads a text file named sample.txt.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.
"""

def read_sample_file():
    try:
        with open("sample.txt", "r") as file:
            print("File opened successfully!\n")
            print("File contents:")
            for idx, line in enumerate(file, start=1):
                print(f"Line {idx}: {line.strip()}")
    except FileNotFoundError:
        print("Error: The file sample.txt was not found.")

def main():
    print("Program to open and read sample.txt")
    read_sample_file()

if __name__ == "__main__":
    main()
