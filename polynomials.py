import numpy as np

# 1. Polynomial ke coefficients ko float me read karna
coefficients = list(map(float, input().split()))

# 2. X ki value ko read karna jahan polynomial evaluate karna hai
x = float(input())

# 3. np.polyval() ka use karke value nikalna aur print karna
print(np.polyval(coefficients, x))