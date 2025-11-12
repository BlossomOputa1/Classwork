while True:
    a = int(input("Enter the first number: "))
    operator = input("Enter operator (*, +, -, /) or 'q' to quit: ")

    if operator.lower() == 'q':
        print("Exiting calculator. Goodbye!")
        break

    b = int(input("Enter the second number: "))

    if operator == "+":
        print(f"Result: {a + b}")
    elif operator == "-":
        print(f"Result: {a - b}")
    elif operator == "*":
        print(f"Result: {a * b}")
    elif operator == "/":
        if b != 0:
            print(f"Result: {a / b}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator. Please use +, -, *, or /.")

    print()  # Blank line for readability
