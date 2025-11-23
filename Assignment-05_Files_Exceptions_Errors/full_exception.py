def divide_numbers(a, b):
    if  not isinstance(b,int) or  not isinstance(a,int):
        raise TypeError("Invalid types for division (must be numbers)!")

    try:
        result = a / b
    except ZeroDivisionError:
        print("Caught an error: Cannot divide by zero!")
        return None # Return None to indicate failure
    except TypeError:
        print("Caught an error: Invalid types for division (must be numbers)!")
        return None
    else:
        print("Division successful!")
        return result
    finally: # This block ALWAYS runs
        print("--- Division attempt finished. ---")

def main():
    print("Scenario 1: Successful division")
    res1 = divide_numbers(10, 2)
    if res1 is not None:
        print(f"Result: {res1}\n")
    print("Scenario 2: Division by zero")
    res2 = divide_numbers(10, 0)
    if res2 is not None:
        print(f"Result: {res2}\n")
    print("Scenario 3: Type error")
    res3 = divide_numbers(10, "two")
    if res3 is not None:
        print(f"Result: {res3}\n")
if __name__ == '__main__':
    main()