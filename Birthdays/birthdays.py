birthdays = {}

while True:
    
    name = input(">")

    if name in birthdays:

        print(name)

    else:

        birthday = str(input("Enter Birthday\n>"))

        birthdays[name] = birthday

    
