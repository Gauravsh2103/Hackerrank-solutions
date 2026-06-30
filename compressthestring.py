# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

# Reading the input string
s = input()

# groupby consecutive same characters ko group karta hai
# key = character, group = wo saare consecutive characters ka iterator
result = [(len(list(group)), int(key)) for key, group in groupby(s)]

# Output ko space-separated format me print karna
print(*result)
