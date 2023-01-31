def calculator():

    # Prompt user to enter numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user for the operation
    operation = input("What operation would you like to perform (+, -, *, /): ")

    # Perform the requested operation
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    else:
        # If the operation is not recognized
        print("Invalid request")

# Call the calculator function
calculator()