import math
from functools import reduce

def find_gcd(numbers):
    return reduce(lambda x, y: math.gcd(x, y), numbers)

# Get user input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Print the GCD
print(f"The GCD of the numbers is {find_gcd(numbers)}")
