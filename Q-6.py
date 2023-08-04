def even_filter(lst):
    # filter out odd numbers
    return [num for num in lst if num % 2 != 0]

def odd_filter(dictionary):
    # filter out even numbers
    return {k: v for k, v in dictionary.items() if v % 2 == 0}

# User defined list
user_list = list(map(int, input("Enter numbers for the list, separated by spaces: ").split()))
print("List with odd numbers: ", even_filter(user_list))

# User defined dictionary
user_dict = {}
n = int(input("Enter number of items in the dictionary: "))
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    user_dict[key] = value
print("Dictionary with even values: ", odd_filter(user_dict))
