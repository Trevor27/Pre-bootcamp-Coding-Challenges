def vowels():

    myString = str(input("Enter a string: "))

    myString.lower()
    
    for vowel in myString:
        if vowel in 'aeiou':
            print(vowel)

vowels()
