# Enter your code here. Read input from STDIN. Print output to STDOUT
# Reading n and m (dimensions)
n, m = map(int, input().split())

# Reading the main array
arr = list(map(int, input().split()))

# Reading Set A and Set B (Sets me search O(1) hota hai, isliye set use karna zaroori hai)
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

# Initializing happiness
happiness = 0

# Calculating final happiness
for num in arr:
    if num in set_a:
        happiness += 1
    elif num in set_b:
        happiness -= 1

# Printing the result
print(happiness)
