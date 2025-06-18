a = 5
b = 10
a, b = b, a
print("After exchanging: a =", a, ", b =", b)

x = 1
y = 2
z = 3
x, y, z = z, x, y
print("After circulating: x =", x, ", y =", y, ", z =", z)

import math
x1, y1 = 3, 4
x2, y2 = 7, 1
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between points:", distance)
