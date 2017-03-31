"""
Input: A string of characters that maybe a word or a sentence
Output: The same string of characters but with its vowels swapped with random vowels

"""

from random import choice

vowels = ('a','e','i','o','u')

err = "An error occured"


while True:

    try:

        output = ""

        prompt = str(input(">"))

        
    except Exception as e:

        print(err)
        print(e)
        

    else:

        if prompt == 0:

            break

        else:

            for letter in prompt:

                if letter not in vowels:

                    output += letter

                else:

                    temp = choice(vowels)

                    while temp == letter:

                        temp = choice(vowels)

                    else:

                        output += temp

            
            print(output)
