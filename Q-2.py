def convert_paragraph_to_list():
    # Take the paragraph from user
    paragraph = input("Enter a paragraph: ")

    # Split the paragraph into words
    words = paragraph.split()

    # Store words with more than 4 letters in a new list
    long_words = [word for word in words if len(word) > 4]

    return long_words

print(convert_paragraph_to_list())
