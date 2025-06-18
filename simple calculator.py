def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = add(x, y)
elif operator == '-':
    result = subtract(x, y)
elif operator == '*':
    result = multiply(x, y)
elif operator == '/':
    result = divide(x, y)
else:
    result = "Error: Invalid operator"

print("Result:", result)
