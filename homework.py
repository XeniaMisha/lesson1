# # welcome = input('what is your name?')
# # print('Hi ' + welcome)

# # age = input('How old are you?')
# # print(f'You have only {age} years!')

# a = 10
# b = 20
# c = a + b
# print(c)

# a = 20
# b = 10
# c = a - b
# print(c)

# a = 3
# b = 11
# c = a * b
# print(c)

# a = 8
# b = 2
# c = a ** b
# print(c)

# a = 16
# b = 2
# c = a / b
# print(c)

# a = 1.30
# b = 2.70
# c = a + b
# print(c)

# a = 5
# b = 11
# c = a < b
# d = a > b
# e = a == b
# h = a != b
# j = a <= b
# k = a >= b
# print(c, d, e, h, j, k)

# a = 'Hello'
# b = 'World'
# print(a + b)

# a = 'Hello'
# b = 'World'
# print(a + ' ' + b + '!')

# a = 'Hello'
# b = 'World'
# print(len(f'{a} {b}!'))

# a = "HELLLLO".lower()
# print(a)

# b = "hello".upper()
# print(b)

# c = 'hello'.capitalize()
# print(c)

# a = '   hello    '.upper().strip()
# print(a)

# b = '  HELLO XENIA    '.lower().strip().capitalize()
# print(b)

# a = 'H2llo X2nia'.replace('2', 'e')
# print(a)

# a = 'Hello Xeniam'.replace('m', '')
# print(a)

# a = 'Hello a todos'.replace('a todos', 'everybody')
# print(a)

# a = 'Hello PYTHON'.lower().replace('python', 'world')
# print(a)

# a = 'estoy.aqui.en.casa'
# print(a.split('.'))

# a = 'estoy aqui aqui para decirte'
# print(a.split(' '))

# a = 'por fin puedo sentir'
# print(len(a.split(' ')))

# a = None
# b = 1
# c = a is None
# d = b is None
# e = a == None
# f = a != None
# print(c, d, e, f)

# a = type(2)
# b = type('2')
# c = type(2.0)
# d = type('hello')
# e = type(1 == 1)
# print(a, b, c, d, e)

# user_data = int(input('What is your year of birthday?'))
# age = 2023 - user_data
# print(f'You have {age} years old')

# a = 2
# print(float(a))

# a = 2
# print(str(a))

# a = 2
# print(bool(a))

# print(float('1'))
# print(int('2.5'))

# products = ['apple', 'orange', 'grapes']
# print(len(products))

# to_do_list = ['piano',
#             'knitting',
#             'sport'
# ]
# to_do_list.append('walking')
# print(to_do_list)

# lists = ['1', '2', '3', '4']
# lists.append('5')
# print(lists)

# lists = ['1', '2', '3', '4']
# print(len(lists))

# lists = ['1', '2', '3', '4']
# lists.append('5')
# print(len(lists))

# lists = ['1', '2', '3', '4', '1']
# lists.append('1')
# print(lists.count('1'))

# to_do_list = ['piano',
#             'knitting',
#             'sport'
# ]
# to_do_list.append('walking')
# print(to_do_list[3])

# to_do_list = ['piano',
#             'knitting',
#             'sport'
# ]
# to_do_list.append('walking')
# print(to_do_list[1:3])
# print(to_do_list[0:4])
# print(to_do_list[:3])
# print(to_do_list[-2])

# to_do_list = ['piano',
#             'knitting',
#             'sport'
# ]
# to_do_list.append('walking')
# print(to_do_list.index('piano'))

# to_do_list = ['piano',
#             'knitting',
#             'sport'
# ]
# to_do_list.append('walking')
# to_do_list.sort()
# print(to_do_list)

# to_do_list = ['piano',
#             'knitting',
#             'sport',
#             'box',
#             'piano'
# ]
# to_do_list.append('walking')
# del to_do_list[1]
# to_do_list.remove('piano')
# print(to_do_list)

# list_of_numbers = [3, 5, 7, 9, 10.5]
# list_of_numbers.append('Python')
# print(list_of_numbers[0])
# print(list_of_numbers[-1])
# print(list_of_numbers[2:5])
# del list_of_numbers[5]
# print(list_of_numbers)

# total_list = ['1', '2', '3', '4', 'apple', 'lemon', 'watermelon', 'apple']
# total_list.append('sugar')
# total_list.sort()
# print(total_list.count('apple'))
# print(total_list[:8])
# print(total_list[-4])
# print(total_list[3:6])
# print(total_list.index("watermelon"))
# print('lemon' in total_list)
# del total_list[4]
# print(total_list)

# my_list = [1, 2, 3, 2, 4, 2]
# del my_list[3]
# print(my_list)

# product = {'name': 'Iphone',
#             'stock': '25',
#             'precio': 65432.1
# }
# print(len(product))


# product = {'name': 'Iphone',
#             'stock': '25',
#             'precio': 65432.1
# }
# product ['memory'] = 64
# product ['color'] = 'black', 'white', 'blue'
# product['name'] = 'Iphone 13'
# print(product)

# product = {'name': 'Iphone',
#             'stock': '25',
#             'precio': 65432.1
# }
# product ['memory'] = 64
# product ['color'] = 'black', 'white', 'blue'
# product['name'] = 'Iphone 13'
# print(product['name'])
# print(product['color'])
# print(product.get('discount'))

# weather = {
#     'city': 'Moscow',
#     'temperature': '20'
# }
# print(weather['city'])
# weather['temperature'] = int('20') - 5
# print(weather.get('country', 'Rusia'))
# weather['date'] = '27.05.2023'
# print(weather)


# weather = {
#     'city': 'Moscow',
#     'temperature': '20'
# }
# print(weather['city'])
# weather['temperature'] = int('20') - 5
# print(weather)
# print(weather.get('country', 'Rusia'))
# weather['date'] = '20.05.2023'
# print(weather)

# my_name = 'Xenia'
# print(my_name)

# numbers = [3, 5, 7, 9, 10.5, 9]
# numbers.append('Python')
# print(numbers)
# print(len(numbers))
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2:5])
# print(3 in numbers)
# print(2 not in numbers)
# numbers.remove(9)
# print(numbers)
# del numbers[0]
# print(numbers)

# products = {
#     'name': 'iphone 13',
#     'stock': 24,
#     'price': 65432.1
#     }
# print(products.get("discount", 0))
# print(products)
# print(len(products))


# foods = {"name": "potato", "weight": 2, "price": 3}
# foods["type"] = "fresh"
# foods["name"] = "tomato"
# print(foods["price"])
# print(foods.get("potato"))
# print(foods.get("origen", "Italia"))
# del foods["type"]
# print(foods)
# sort_tomato = ["red", "green", "black"]
# foods["types"] = sort_tomato
# print(foods)
# sort_tomato.append("cherry")
# print(foods)


# foods = [
#     {"name": "potato", "weight": 2, "price": 3},
#     {"name": "tomato", "weight": 1, "price": 4},
#     {"name": "cucumber", "weight": 1, "price": 2},
# ]
# print(foods)
# print(foods[2])
# foods[1]["price"] = foods[1]["price"] - 1
# print(foods[1]["price"])
# print(type(foods))
# print(type(foods[2]))


# weather = {"city": "Москва", "temperature": 20}
# print(weather["city"])
# weather["temperature"] = weather["temperature"] - 5
# print(weather)




# def discounted(price, discount, max_dis = 12):
#     price = abs(price)
#     discount = abs(discount)
#     max_dis = abs(max_dis)
#     if max_dis >= 100:
#         raise ValueError('Imposible')
#     if discount >= max_dis:
#         price_w_doscount = price
#     else:
#         price_w_doscount = price - price * discount / 100
#     print(price_w_doscount)

# discounted(100, 5)


# def get_summ(one, two, delimiter = '&'):
#     result = one + delimiter + two
#     return (result.upper())

# result = get_summ('Learn', 'python')
# print(result)

def weather(temperature):

    if temperature < 0:
        return 'холодно'
    elif temperature >= 0 and temperature < 15:
        return 'прохладно'
    elif temperature >= 15 and temperature < 25:
        return 'тепло'
    else:
        return 'жарко'  
temperature = int(input('Сколько градусов на улице?'))
result = weather(temperature)
print(f'Сейчас на улице {result}') 






