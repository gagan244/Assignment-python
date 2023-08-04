def prodDigits(n):
    product = 1
    while n > 0:
        digit = n % 10
        product *= digit
        n = n // 10
    return product

def MDR(n):
    while n > 9:
        n = prodDigits(n)
    return n

def MPersistence(n):
    count = 0
    while n > 9:
        n = prodDigits(n)
        count += 1
    return count

# Test the functions
n = 86
print(f"MDR of {n} is {MDR(n)}")
print(f"MPersistence of {n} is {MPersistence(n)}")

n = 341
print(f"MDR of {n} is {MDR(n)}")
print(f"MPersistence of {n} is {MPersistence(n)}")
