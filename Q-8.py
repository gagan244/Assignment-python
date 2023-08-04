def checkPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def twinPrime():
    twin_primes = []
    for i in range(2, 1000):
        if checkPrime(i) and checkPrime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

# Test the function
print(twinPrime())
