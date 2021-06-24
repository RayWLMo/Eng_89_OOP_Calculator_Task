# Functional Calculator
## Timings
30 - 60 Minutes
## Summary
Amazing you now know functions, let's make a functional calculator.
## Tasks
* Complete the core tasks
- Practice using, defining and calling functions
```python
# Create a class called Calculator

# functions

# Build a basic functional calculator
# Core 1: build function containing
    # add,
    # subtract,
    # multiply,
    # divide.

# Create a file for child class called Functional_calculator
# import calculator class and inherit all the functionality 
# Core 2: Build more functions for
    # area of a circle
    # area of a square
    # area of an equilateral triangle
```
## Solution
Defining the `Calculator` class and the basic calculator functions
```py
class Calculator:

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b
```
Prompting the user for numbers to use
```python
query_prompt = True
first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))
while query_prompt:
    operator = input("what operation would you like to do (add, subtract, multiply, divide, area)?"
                     "or type 'exit' to close the program:  ")
    if operator.lower() == "add":
        print(Calculator.add(first_number, second_number))
        query_prompt = False
    elif operator.lower() == "subtract":
        print(Calculator.subtract(first_number, second_number))
        query_prompt = False
    elif operator.lower() == "multiply":
        print(Calculator.multiply(first_number, second_number))
        query_prompt = False
    elif operator.lower() == "divide":
        print(Calculator.divide(first_number, second_number))
        query_prompt = False
    elif operator.lower() == "exit":
        print("Thank you for using this program")
        break
    else:
        print("The input is invalid, please try again.")
```
### Calculator for shape area
Importing math module and Calculator class created in step 1
```py
from calculator import Calculator
import math
```
Defining the `Functional_Calculator` class
```py
class Functional_Calculator(Calculator):

    def __init__(self):
        super().__init__()  # Inheriting from Calculator

    def Circle_Area(r):
        return "The area of the circle is " + str(math.pi * (r ** 2))

    def Square_Area(l):
        return "The area of the square is " + str(l ** 2)

    def Triangle_Area(b, h):
        return "The area of the triangle is " + str(0.5 * b * h)
```

Original `calculator` prompt with added option `area`
- `area` directs the user to another while loop where the shape can be selected
- The class called is now `Functional_Calculator` instead of `Calculator`
```py
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
```
