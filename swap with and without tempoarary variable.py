# With temporary variable
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
temp = a
a = b
b = temp
print("After swapping with temp variable: a =", a, ", b =", b)

# Without temporary variable
a = int(input("Enter value of a again: "))
b = int(input("Enter value of b again: "))
a, b = b, a
print("After swapping without temp variable: a =", a, ", b =", b)
