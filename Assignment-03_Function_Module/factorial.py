def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "None"
    else:
        return n * factorial(n-1)

def factorial_iter(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def main():
    print("----Factorial Program----")
    while True:
        try:
            fact = int(input("Enter a number: "))
            if fact < 0:
                print("Invalid Input")
                continue
            elif fact >500:
                print(f"Factorial of {fact} is {factorial_iter(fact)}")
            else:
                print(f"Factorial of {fact} is {factorial(fact)}")
            #for continue the application??
            if input("Do You want to continue? (y/n)") =='y':
                continue
            else:
                print("Exiting program. Thank you!")
                break

        except ValueError:
            print("Please enter valid number")

if __name__ == '__main__':
    main()