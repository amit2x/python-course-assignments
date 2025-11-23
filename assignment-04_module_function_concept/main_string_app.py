import string_util
def main():
    print("Using String Util Module")
    while True:
        char = input("Enter a phrase: ")
        print(f"Reverse : {string_util.reverse_string(char)}")
        print(f" Is Palindrome : {string_util.is_palindrome(char)}")
        print(f"Word Count: {string_util.count_words(char)}")

        num = input("Press any number to continue...")
        if num.isdigit():
            continue
        else:
            print("Thankyou for using this  program")
            break

if __name__ == "__main__":
    main()
