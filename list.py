to_do_list = ['cleaning', 'fitness', 'working', 'walking', 'cooking', 'reading']
print(to_do_list)


to_do_list = ['cleaning', 'fitness', 'working', 'walking', 'cooking', 'reading']
print(to_do_list[0])


my_friends = ['Luba', 'Lidia', 'Sergio', 'Tina']
print(my_friends[1])
print()
message = 'My best friend is: ' + my_friends[0].upper() + '!'
print(message)
message = my_friends[1] + ' - is my music teacher'
print(message)
message = 'I met ' + my_friends[2] + ' in 2013'
print(message)
message = 'And ' + my_friends[3] + ' is my neighbor'
print(message)


instruments = ['casio', 'yamaha', 'kawai', 'korg', 'roland']
message = instruments[2].title() + ' is my favorite brand of piano!'
print(message)


instruments = ['casio', 'yamaha', 'artesia', 'korg', 'roland']
instruments[2] = 'kawai'
message = instruments[2].title() + ' is my favorite brand of piano!'
print(message)