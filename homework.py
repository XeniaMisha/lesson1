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

# def weather(temperature):

#     if temperature < 0:
#         return 'холодно'
#     elif temperature >= 0 and temperature < 15:
#         return 'прохладно'
#     elif temperature >= 15 and temperature < 25:
#         return 'тепло'
#     else:
#         return 'жарко'  
# temperature = int(input('Сколько градусов на улице?'))
# result = weather(temperature)
# print(f'Сейчас на улице {result}') 


# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)


# guests = ['kate', 'lucie', 'andrew']
# for guest in guests:
#     print(guest)


# def discounted(price, discount):
#     price_with_discount = price - (price * discount / 100)
#     print(price_with_discount)

# discounted(100, 50)
# discounted(100, 5)


# grades = [4, 5, 3, 4, 5]
# total_grade = sum(grades)
# print("Общая оценка по классу:", total_grade)

# students_scores = [3, 5, 4, 3, 5, 5]

# scores_sum = 0
# for scores in students_scores:
#     scores_sum += scores

# class_scores = scores_sum / len(students_scores)
# print(f'Средняя оценка по классу: {class_scores}')


# # students_scores = [3, 5, 4, 4, 2]

# # scores_sum = 0
# # for score in students_scores:
# #     scores_sum += score
# #     print(scores_sum)
# # scores_avg = scores_sum / len(students_scores)
# # print(f"Средняя оценка {scores_avg}")



# stock = [
# 		{'name': 'iPhone', 'stock': 24, 'price': 65432.1,
#                 'discount': 25},
# 		{'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0,
#                 'discount': 10},
# 		{'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10}
# ]

# def discounted(price, discount, max_dis = 30, phone_name = ''):
#     price = abs(price)
#     discount = abs(discount)
#     max_dis = abs(max_dis)
#     if max_dis >= 100:
#         raise ValueError('Imposible')
#     if discount >= max_dis:
#         return price
#     elif 'iphone' in phone_name.lower() or not phone_name:
#         return price
#     else:
#         return price - price * discount / 100

# for phone in stock:
#     phone['final_price'] = discounted(phone['price'], phone['discount'], phone_name=phone['name'])
    
# print(stock)





# def count_average(students_scores):
#     scores_sum = 0
#     for score in students_scores:
#         scores_sum += score
#     scores_avg = scores_sum / len(students_scores)
#     return scores_avg




# def hello_user():
#     try:
#         while True:
#             user_say = input('Скажи что-нибудь: ')
#             if user_say == 'Пока':
#                 print('Ну пока!')
#                 break
#             else:
#                 print('Сам ты {}'.format(user_say))
#     except KeyboardInterrupt:
#         print('Пока!')

# hello_user()



# def discounted(price, discount, max_discount=20):
#     try:
#         price = float(price)
#         discount = float(discount)
#         max_discount = int(max_discount)
#     except (ValueError, TypeError):
#         raise ValueError('Некорректные аргументы')

#     price = abs(price)
#     discount = abs(discount)
#     max_discount = abs(max_discount)
    
#     if max_discount >= 100:
#         raise ValueError('Слишком большая максимальная скидка')

#     if discount >= max_discount:
#         return price
#     else:
#         return price - (price * discount / 100)


def main(age):
    if age < 7:
        return 'Ты ходишь в детский сад'
    elif age >= 7 and age < 18:
        return 'Ты школьник'
    else:
        return 'Ты учишься в универе или уже работаешь'
    
age = int(input('How old are you?'))
result = main(age)
print(result)


def main(age):
    if age < 7:
        return 'Eres un niñ@'
    elif age >= 7 and age < 18:
        return 'estudias en secundaria o terminas bachillerato'
    else:
        return 'Estuias en Universidad o ya estas trabajando'
    
age = int(input('Cuantos años tienes?'))    
result = main(age)
print(result)


def main(age):
    if age < 7:
        return 'Ты ходишь в детский сад'
    elif age >= 7 and age < 18:
        return 'Ты школьник'
    else:
        return 'Ты учишься в универе или уже работаешь'
    
age = int(input('How old are you?'))
result = main(age)
print(result)


















