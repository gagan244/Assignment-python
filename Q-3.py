def cat_and_dog():
    # Take the string from user
    user_input = input("Enter a string: ")

    # Count occurrences of "cat" and "dog"
    cat_count = user_input.lower().count("cat")
    dog_count = user_input.lower().count("dog")

    # Return True if "cat" and "dog" appear the same number of times
    return cat_count == dog_count

print(cat_and_dog())
