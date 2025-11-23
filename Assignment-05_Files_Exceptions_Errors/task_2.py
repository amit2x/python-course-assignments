"""
Task 2: Write and Append Data to a File

1. Take user input and write it to output.txt
2. Append additional data to the same file
3. Read and display the final content
"""

def write_and_append():
    # Step 1: Get user input
    user_data = input("Enter some data to write into the file: ")

    # Step 2: Write the user data to output.txt
    with open("output.txt", "w") as file:
        file.write(user_data + "\n")

    # Step 3: Append additional data
    with open("output.txt", "a") as file:
        file.write("This is appended data.\n")

    # Step 4: Read and display final content
    with open("output.txt", "r") as file:
        print("\nFinal file contents:")
        print(file.read())

def main():
    write_and_append()

if __name__ == "__main__":
    main()
