import math

# Step 1: Define Functions for Area Calculations

# Function to calculate the area of a rectangle
def area_rectangle(length, width):
    return length * width

# Function to calculate the area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height

# Function to calculate the area of a circle
def area_circle(radius):
    return math.pi * radius ** 2

# Step 2: Get user input based on selected shape
def calculate_area():
    while True:
        print("\nChoose a shape to calculate the area:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Exit")
        
        try:
            choice = int(input("Enter the number of your choice (1-4): "))
            
            if choice == 1:  # Rectangle
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                area = area_rectangle(length, width)
                print(f"The area of the rectangle is: {area:.2f}")
            
            elif choice == 2:  # Triangle
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = area_triangle(base, height)
                print(f"The area of the triangle is: {area:.2f}")
            
            elif choice == 3:  # Circle
                radius = float(input("Enter the radius of the circle: "))
                area = area_circle(radius)
                print(f"The area of the circle is: {area:.2f}")
            
            elif choice == 4:  # Exit
                print("Exiting the program.")
                return  # Exit the function and program
            
            else:
                print("Invalid choice. Please select a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the area calculation based on user selection
calculate_area()
