# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

# Reading the lengths of sides AB and BC
ab = float(input())
bc = float(input())

# Calculating the angle in radians using atan(AB/BC)
# trigonometry ke mutabik angle MBC = angle MCB hai
angle_rad = math.atan(ab / bc)

# Converting radians to degrees
angle_deg = math.degrees(angle_rad)

# Rounding to the nearest integer and adding the degree symbol
# HackerRank requires the '°' symbol at the end
print(f"{round(angle_deg)}{chr(176)}")
