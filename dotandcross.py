import numpy as np

# 1. Matrix ka size (N) read karna
n = int(input())

# 2. Matrix A ke saare elements read karke array banana
matrix_a = np.array([list(map(int, input().split())) for _ in range(n)])

# 3. Matrix B ke saare elements read karke array banana
matrix_b = np.array([list(map(int, input().split())) for _ in range(n)])

# 4. Matrix multiplication (Dot product) calculate karna
result = np.dot(matrix_a, matrix_b)

# 5. Output print karna
print(result)
