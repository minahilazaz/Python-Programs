import math

# Input circumference
circumference = float(input('Enter circumference: '))

# Calculate radius from circumference
radius = circumference / (2 * math.pi)

# Calculate area from radius
area = math.pi * (radius ** 2)

print('Radius of circle is', radius)
print('Area of circle is', area)
