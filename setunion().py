# Enter your code here. Read input from STDIN. Print output to STDOUT\
# Reading English newspaper subscribers
n = int(input())
english = set(map(int, input().split()))

# Reading French newspaper subscribers
m = int(input())
french = set(map(int, input().split()))

# Union operation dono sets ke saare unique elements ko combine kar deta hai
result = english.union(french)

# Printing the total number of unique students
print(len(result))
