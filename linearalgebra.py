import numpy as np

# 1. Matrix ka dimension (N) read karna
n = int(input())

# 2. N rows ko read karke float matrix (2D array) banana
# Determinant hamesha float ya complex numbers par sahi kaam karta hai
matrix = np.array([list(map(float, input().split())) for _ in range(n)])

# 3. numpy.linalg.det() ka use karke determinant nikalna
det_value = np.linalg.det(matrix)

# 4. Output ko 2 decimal places tak round karke print karna
# (HackerRank strict test cases matching ke liye)
print(round(det_value, 2))
