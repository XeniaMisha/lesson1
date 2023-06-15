message = "One of Python's strengths is its diverse community"
print(message)


name = 'Xenia'
print('Hello,' + ' ' + name + '!' + ' ' + 'Would you like to learn some Python today?')
print(f'Hello, {name}! Would you like to learn some Python today?')


my_name = 'Xenia'
my_surname = 'Mishakova'
my_full_name = my_name + ' ' + my_surname
print(my_full_name.upper())
print(my_full_name.lower())
print(my_full_name.title())
print(my_full_name.capitalize())


quote = "Albert Einstein once said, 'A person who never made a mistake never tried anything new.'"
print(quote)


famous_person = 'Albert Einstein'
message = "'A person who never made a mistake never tried anything new.'"
print(famous_person + ' once said, ' + message)
print(f'{famous_person} once said, {message}')


message = ' I say hello! '
print(message)
print()
message = '\tI say hello!'
print(message)
message = '\n\tI \nsay \nhello!'
print(message)
print()
message = ' I say hello! '
print(message.rstrip())
message = ' I say hello! '
print(message.lstrip())
message = ' I say hello! '
print(message.strip())
