# # def discounted(price, discount):
# #     price_with_discount = price - (price * discount / 100)
# #     print(price_with_discount)

# def discounted(price, discount):
#     if discount >= 100:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price * discount / 100)
#     print(price_with_discount)

# discounted(100, 101)

# def discounted(price, discount):
#     price = abs(price)
#     discount = abs(discount)
#     if discount >= 100:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price * discount / 100)
#     return price_with_discount

# def discounted(price, discount, max_discount=20):
#     price = abs(price)
#     discount = abs(discount)
#     max_discount = abs(max_discount)
#     if max_discount >= 100:
#         raise ValueError('Слишком большая максимальная скидка')
#     if discount >= max_discount:
#         return price
#     else:
#         return price - (price * discount / 100)
#     # discounted(100, 50)
#     discounted(100, 50, max_discount=60)



# def get_summ(one, two, delimiter='&'):
#     result = one + delimiter + two
#     return result.upper()


# result = get_summ('Learn', 'python') 
# print(result) 

# def format_price(price):
#     price = int(price)
#     return f'Цена: {price} руб.'


# result = format_price(56.24)
# print(result) 

# balance = 100
# price = 50

# if balance > price:
#     print('Одобряем оплату покупки')
# else:
#     print('Пожалуйста, пополните баланс!')


def check_weather(temperature):
    if temperature < 0:
        return 'На улице холодно'
    elif temperature >= 0 and temperature < 15:
        return 'На улице прохладно'
    elif temperature >= 15 and temperature < 25:
        return 'На улице тепло'
    else:
        return 'На улице жарко'

print(check_weather(-1)) # На улице холодно
print(check_weather(8)) # На улице прохладно
print(check_weather(21)) # На улице тепло
print(check_weather(32)) # На улице жарко



def discounted(price, discount, max_discount=30, phone_name=''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)
    

new_price = discounted(100000, 10, phone_name='iPhone 12')
print(new_price)

new_price = discounted(40000, 20, phone_name='Xiaomi Mi11')
print(new_price)

new_price = discounted(100, 10)
print(new_price)












