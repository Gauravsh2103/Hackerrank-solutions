# Enter your code here. Read input from STDIN. Print output to STDOUT
# Reading English newspaper subscribers count and roll numbers
n = int(input())
english = set(map(int, input().split()))

# Reading French newspaper subscribers count and roll numbers
m = int(input())
french = set(map(int, input().split()))

# Intersection se sirf wahi roll numbers milenge jo dono sets me COMMON hain
common_students = english.intersection(french)

# Un students ka total count print karna
print(len(common_students))