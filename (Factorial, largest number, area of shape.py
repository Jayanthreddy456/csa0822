def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def largest_number(numbers):
    return max(numbers)

def area_of_shape(shape, *dimensions):
    if shape == "circle":
        return 3.1416 * dimensions[0] ** 2
    elif shape == "rectangle":
        return dimensions[0] * dimensions[1]
    elif shape == "triangle":
        return 0.5 * dimensions[0] * dimensions[1]
    else:
        return "Invalid shape"

n = int(input("Enter number to find factorial: "))
print("Factorial:", factorial(n))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest number:", largest_number(numbers))

shape = input("Enter shape (circle/rectangle/triangle): ")
if shape == "circle":
    r = float(input("Enter radius: "))
    print("Area:", area_of_shape(shape, r))
elif shape in ["rectangle", "triangle"]:
    a = float(input("Enter first dimension: "))
    b = float(input("Enter second dimension: "))
    print("Area:", area_of_shape(shape, a, b))
else:
    print("Invalid shape")
