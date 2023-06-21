my_fav_pizzas = ['pepperoni', 'four cheeses', 'hawaiian', 'margarita']
for pizza in my_fav_pizzas:
    print(pizza)


my_fav_pizzas = ['pepperoni', 'four cheeses', 'hawaiian', 'margarita']
for pizza in my_fav_pizzas:
    print('I like ', pizza)

print('\nI really like pizza!')
print()

animals = ['dog', 'cat', 'turtle', 'rabbit']
for animal in animals:
    print(animal)


animals = ['dog', 'cat', 'turtle', 'rabbit']
for animal in animals:
    print('A ', animal, 'would make a great pet!')

print('\nAny of these animals would make a great pet')
print()

for numbers in range(1, 21):
    print(numbers)


numbers = list(range(1, 1000001))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


numbers = list(range(1, 21, 2))
for number in numbers:
    print(number)


numbers = list(range(3, 30, 3))
for number in numbers:
    print(number)


numbers = list(range(1, 11))
for number in numbers:
    print(number**3)


numbers = [number**3 for number in numbers]
print(numbers)