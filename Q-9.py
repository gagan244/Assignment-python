import math

def factorial(n):
    return math.factorial(n)

def permutation(n, r):
    return factorial(n) / factorial(n - r)

def combination(n, r):
    return permutation(n, r) / factorial(r)

# Test the functions
n = 5
r = 3

print(f"Permutations of {n} objects taken {r} at a time: {permutation(n, r)}")
print(f"Combinations of {n} objects taken {r} at a time: {combination(n, r)}")
