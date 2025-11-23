from unicodedata import digit


def power_num(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base * power_num(base, exponent-1)

def main():
    print("This is Power Number Module")
    while True:
        try:
            base = int(input("Enter a base: "))
            exponent = int(input("Enter a exponent: "))
        except ValueError:
            print("Invalid input")
            continue

        print("Power of base: ", power_num(base,exponent))

        num = input("Press any number to continue...")
        if num.isdigit():
            continue
        else:
            print("Thankyou for using this program")
            break

if __name__ == "__main__":
    main()