# Enter your code here. Read input from STDIN. Print output to STDOUT
# Reading English newspaper subscribers count and roll numbers
n = int(input())
english = set(map(int, input().split()))

# Reading French newspaper subscribers count and roll numbers
m = int(input())
french = set(map(int, input().split()))

# .difference() se sirf wahi roll numbers milenge jo English me hain par French me nahi
only_english = english.difference(french)

# Un students ka total count print karna
print(len(only_english))