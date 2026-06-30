# Reading the total number of country stamps
n = int(input())

# Creating an empty set to store unique countries
countries = set()

# Loop chala kar har country ka naam read karna aur set me add karna
for _ in range(n):
    countries.add(input())

# Set ki length hi unique countries ka count hai
print(len(countries))
