from math import sqrt
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))
b1 = (b * b)
d1 = (a * c)
d2 = (d1 * 4)
d3 = (b1 - d2)
a1 = (2 * a)
x = (-b + sqrt(d3)) / a1
y = (-b - sqrt(d3)) / a1
print(f"The roots are {x} and {y}")