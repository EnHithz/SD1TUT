#nested if solution
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Invalid operator. Please use +, -, *, or /.")

if operator != '/' or (operator == '/' and num2 != 0):
    print(f"Result: {num1} {operator} {num2} = {result}")
