vowels = ('a','e','i','o','u')

prompt = input(">")

output = ""

for letter in prompt:

    if letter in vowels:

        print("Found " + letter + " removing " + letter)

    if letter not in vowels:

        output += letter

print(output)
