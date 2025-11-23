import math
def calculate_square_area(side):
    return side*side

def calculate_rectangle_area(side1, side2):
    return side1*side2

def calculate_circle_area(radius):
    return math.pi*radius**2

def main():
    print("Welcome to the calculator")

    print("""
        1. Area of Square
        2. Area of Rectangle
        3. Area of Circle
        4. Exit
        """)

    while True:
       try:
           option = int(input("Please enter your choice: "))
       except ValueError:
            print("please enter a valid number")
            continue

       if option == 1:
           side = int(input("enter square side length: "))
           area_of_square = calculate_square_area(side)
           print(f"The area of square is: {area_of_square}")
       elif option == 2:
            length = int(input("enter length of rectangle: "))
            breadth = int(input("enter breadth of rectangle: "))
            area_of_rectangle = calculate_rectangle_area(length, breadth)
            print(f"The area of rectangle is: {area_of_rectangle}")
       elif option == 3:
            radius = int(input("enter radius of circle: "))
            area_of_circle = calculate_circle_area(radius)
            print(f"The area of circle is: {area_of_circle}")
       elif option == 4:
            print("Thank you for using this program")
            break
       elif option < 0 or option > 4:
            print("please enter a valid option")
            continue


if __name__ == "__main__":
    main()
