from calculator import Calculator
import math


class Functional_Calculator(Calculator):

    def __init__(self):
        super().__init__()

    def Circle_Area(r):
        return "The area of the circle is " + str(math.pi * (r ** 2))

    def Square_Area(l):
        return "The area of the square is " + str(l ** 2)

    def Triangle_Area(b, h):
        return "The area of the triangle is " + str(0.5 * b * h)


user = Functional_Calculator()
query_prompt = True
first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))
while query_prompt:
    operator = input("what operation would you like to do (add, subtract, multiply, divide, area)?"
                     "or type 'exit' to close the program:  ")
    if operator.lower() == "add":
        print(Functional_Calculator.add(first_number, second_number))
        query_prompt = False
    elif operator.lower() == "subtract":
        print(Functional_Calculator.subtract(first_number, second_number))
        query_prompt = False
    elif operator.lower() == "multiply":
        print(Functional_Calculator.multiply(first_number, second_number))
        query_prompt = False
    elif operator.lower() == "divide":
        print(Functional_Calculator.divide(first_number, second_number))
        query_prompt = False
    elif operator.lower() == "exit":
        print("Thank you for using this program")
        break
    elif operator.lower() == "area":
        while query_prompt:
            shape = input("What shape would you like to find the area of (circle, square, triangle)?  ")
            if shape.lower() == "circle":
                print(Functional_Calculator.Circle_Area(first_number))
                break
            if shape.lower() == "square":
                print(Functional_Calculator.Square_Area(first_number))
                break
            if shape.lower() == "triangle":
                print(Functional_Calculator.Triangle_Area(first_number, second_number))
                break
            else:
                print("The shape inputted is invalid, please try again.")
    else:
        print("The input is invalid, please try again.")