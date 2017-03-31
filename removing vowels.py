vowels = ('a','e','i','o','u')

prompt = input(">")

output = ""

for letter in prompt:

    if letter not in vowels:

        output += letter

print(output)
