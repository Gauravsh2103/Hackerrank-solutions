
import numpy

# Reading dimensions
n, m = map(int, input().split())

# Creating the array as integer array first
my_array = numpy.array([list(map(int, input().split())) for _ in range(n)])

# Explicitly calculating and formatting as per HackerRank's exact test requirements:
print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))

# HackerRank requires legacy/standard output match without the rounding glitch of 1.13 setting
std_val = numpy.std(my_array)
print(round(std_val, 11) if std_val != 0 else std_val)