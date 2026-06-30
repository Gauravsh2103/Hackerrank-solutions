# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

arr = list(map(int, input().split()))
print(numpy.array(arr).reshape(3, 3))
