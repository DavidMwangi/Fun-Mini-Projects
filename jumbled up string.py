"""

Input: A string
Output: Jumbled up version of the string

"""

from random import randint

prompt = str(input(">"))
             
letters = list(prompt)

iteration = 0

output = ""
             
for letter in range(0, len(letters)):

    output += letters.pop(randint(0, len(letters)-1))

print(output)
