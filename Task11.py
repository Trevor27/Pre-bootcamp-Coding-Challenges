def commonChars():

    str1 = input("Enter a word: ")
    str2 = input("Enter a word: ")

    for char in str1:
        if char in str2:
            print(char)

commonChars()
