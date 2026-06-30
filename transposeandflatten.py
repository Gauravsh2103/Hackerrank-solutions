# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

n, m = map(int, input().split())

arr = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.transpose(arr))
print(arr.flatten())