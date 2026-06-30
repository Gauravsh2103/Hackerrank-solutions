# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())

is_strict_superset = True

for _ in range(n):
    B = set(map(int, input().split()))
    if not A.issuperset(B) or A == B:
        is_strict_superset = False

print(is_strict_superset)