from math import tan, pi

n = float(input("Enter the length of each side of the ploygon: "))
s = float(input("Enter the number of the sides: "))

area = (n * s ** 2) / (4 * tan(pi / n))

print('The area of the polygon is', area)