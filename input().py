# Reading x and k
x, k = map(int, input().split())

# Reading the polynomial expression as a string
expression = input()

# eval() string expression ko evaluate karega x ki value use karke
if eval(expression) == k:
    print(True)
else:
    print(False)
