def nand(A, B):
    return not (A and B)

# Test cases
print(nand(True, True))  # Outputs: False
print(nand(True, False))  # Outputs: True
print(nand(False, True))  # Outputs: True
print(nand(False, False))  # Outputs: True
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))  # Outputs: [0, 1]
