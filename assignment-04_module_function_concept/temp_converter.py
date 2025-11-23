def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)*5/9
def celsius_to_fahrenheit(celsius):
    return (celsius - 32)*5/9
def main():
    while True:
        try:
            temp =  float(input("please enter temperature in Celsius:"))
            print(f"the temperature {temp} degree Celsius is {fahrenheit_to_celsius(temp)} degree Fahrenheit")
            temp_fahrenheit = int(input("please enter temperature in Fahrenheit:"))
            print(f"the temperature {temp_fahrenheit} degree fahrenheit is {fahrenheit_to_celsius(temp_fahrenheit)} degree celsius")
            print("Do you want to continue? Enter Y/ N")
            con = input("please enter Y/ N")
            if con == "Y":
                continue
            else:
                break
        except ValueError:
            print("please enter a valid temperature")
            break

    print("Thank You, Good Bye")

if __name__ == "__main__":
    main()
