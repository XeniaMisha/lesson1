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


guests = ['Luba', 'Mariana', 'Katia', 'Lena']
print('\nHello, my dear ' + guests[0] + '! See you today at 8!')
print('\nHello, my dear ' + guests[1] + '! See you today at 8!')
print('\nHello, my dear ' + guests[2] + '! See you today at 8!')
print('\nHello, my dear ' + guests[3] + '! See you today at 8!')
print()
print(guests[3], "can't come")
guests[3] = 'Sveta'
print('\nHello, my dear ' + guests[0] + '! See you today at 8!')
print('\nHello, my dear ' + guests[1] + '! See you today at 8!')
print('\nHello, my dear ' + guests[2] + '! See you today at 8!')
print('\nHello, my dear ' + guests[3] + '! See you today at 8!')
print('\nInvite more guests')
guests.insert(0, 'Erich')
guests.insert(3, 'Yaric')
guests.append('Igor')
print(len(guests))
print('\nHello, my dear ' + guests[0] + '! See you today at 8!')
print('\nHello, my dear ' + guests[1] + '! See you today at 8!')
print('\nHello, my dear ' + guests[2] + '! See you today at 8!')
print('\nHello, my dear ' + guests[3] + '! See you today at 8!')
print('\nHello, my dear ' + guests[4] + '! See you today at 8!')
print('\nHello, my dear ' + guests[5] + '! See you today at 8!')
print('\nHello, my dear ' + guests[6] + '! See you today at 8!')
print('\nI can only invite two guests')
cant_invite = guests.pop()
print("\nI'm sorry,", cant_invite, "but I can't invite you today")
cant_invite = guests.pop()
print("\nI'm sorry,", cant_invite, "but I can't invite you today")
cant_invite = guests.pop()
print("\nI'm sorry,", cant_invite, "but I can't invite you today")
cant_invite = guests.pop()
print("\nI'm sorry,", cant_invite, "but I can't invite you today")
cant_invite = guests.pop()
print("\nI'm sorry,", cant_invite, "but I can't invite you today")
print('\nOur meeting is still on, ', guests[0])
print('\nOur meeting is still on, ', guests[1])
del guests[1]
del guests[0]
print(guests)


to_visit = ['Italy', 'France', 'Ireland', 'Norway', 'Finland', 'UK', 'Germany']
print(sorted(to_visit))
print(to_visit)
print(sorted(to_visit, reverse=True))
to_visit.reverse()
print(to_visit)
to_visit.reverse()
print(to_visit)
to_visit.sort()
print(to_visit)
to_visit.sort(reverse=True)
print(to_visit)


guests = ['Luba', 'Mariana', 'Katia', 'Lena']
print(len(guests))