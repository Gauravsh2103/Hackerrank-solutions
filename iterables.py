# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

# 1. Total number of elements
n = int(input())

# 2. The list of characters
letters = input().split()

# 3. Number of elements to select
k = int(input())

# Saare possible combinations (groups of size K) nikalna
all_combinations = list(combinations(letters, k))

# Wo combinations count karna jisme kam se kam ek 'a' ho
favorable_cases = 0
for combo in all_combinations:
    if 'a' in combo:
        favorable_cases += 1

# Probability = Favorable Cases / Total Cases
probability = favorable_cases / len(all_combinations)

# Output ko 4 decimal places tak print karna
print(f"{probability:.4f}")
