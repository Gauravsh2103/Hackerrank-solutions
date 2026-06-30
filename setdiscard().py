# Reading the number of elements in the set
n = int(input())

# Creating the set with initial integer elements
s = set(map(int, input().split()))

# Reading the number of commands
num_commands = int(input())

# Loop to execute each command dynamically
for _ in range(num_commands):
    command = input().split()
    
    # command[0] method ka naam hoga (pop, remove, discard)
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))

# Printing the sum of remaining elements in the set
print(sum(s))