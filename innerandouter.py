import numpy as np

# 1. Dono input arrays ko integers me read karna
a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))

# 2. Inner product nikalna aur print karna
print(np.inner(a, b))

# 3. Outer product nikalna aur print karna
print(np.outer(a, b))
