# Basic Calculator Program with predefined values

# Function to perform the arithmetic operation
def calculator():
    # numbers and operation
    num1 = 5  # 
    num2 = 10  # 
    operation = "+"  #  operation
    
    # Perform the calculation based on the  operation
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please use +, -, *, or /.")

# Call the calculator function
calculator()
