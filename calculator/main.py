"""
The program takes user input, performs a mathematical operation
and returns the results of the operation

input:  expects two numbers and an operator
        Operators are limited to + - / *

output: returns a number
"""

def calcualtor():
    num1 = input("Enter a number: ")
    print(f"You entered {num1}")
    num2 = input("Enter a second number: ")
    print(f"You entered {num2}")
    op = input("Enter an operator: (+, - , / , =): ")
    print(f"You choose {op}")

    while op not in ["+", "-", "/", "*"]:
        print("Please enter a valid mathematical operator (e.g +, -, /, *)")
        op = input("Enter an operator")
    
    match op:
        case "+":
            print("The answer is: ", float(num1) + float(num2))
        
        case "-":
            print("The answer is: ", float(num1) - float(num2))
        
        case "*":
            print("The answer is: ", float(num1) * float(num2))
        
        case "/":
            print("The answer is: ", float(num1) * float(num2))
        
        case _:
            return float(num1) + float(num2)

if __name__ == "__main__":
    calcualtor()