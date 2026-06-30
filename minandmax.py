# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

# Reading dimensions N and M
n, m = map(int, input().split())

# Creating the 2D array from input
my_array = numpy.array([list(map(int, input().split())) for _ in range(n)])

# Step 1: Find the min along axis 1 (rows)
min_axis_1 = numpy.min(my_array, axis=1)

# Step 2: Find the max of that result
result = numpy.max(min_axis_1)

# Printing the final output
print(result)
