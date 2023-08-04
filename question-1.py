def merge_lists_to_dict():
    # Take the first list from user
    list1 = input("Enter elements of the first list, separated by comma: ").split(',')
    # Try to convert numbers in the list to integers
    for i in range(len(list1)):
        try:
            list1[i] = int(list1[i])
        except ValueError:
            list1[i] = list1[i].strip()

    # Take the second list from user
    list2 = input("Enter elements of the second list, separated by comma: ").split(',')
    # Try to convert numbers in the list to integers
    for i in range(len(list2)):
        try:
            list2[i] = int(list2[i])
        except ValueError:
            list2[i] = list2[i].strip()

    # Check if both lists have same length
    if len(list1) != len(list2):
        print("Both lists must have the same length.")
        return

    # Check if list1 has unique elements
    if len(list1) != len(set(list1)):
        print("The first list must contain unique elements.")
        return

    # Create the dictionary
    my_dict = dict(zip(list1, list2))

    return my_dict

print(merge_lists_to_dict())
