from data import products, people, numbers

# import
from functools import reduce

# add numbers
# ac = accumulator
add_numbers = reduce(lambda ac, i:i + ac, numbers, 0)

print(f'add numbers: { add_numbers }')

# add prices
add_prices = reduce(lambda ac, product: product['price'] + ac, products, 0)

print(f'add prices: { add_prices }')
print(f'average prices: { add_prices / len(products) }')

# avegare age people
add_age = reduce(lambda ac, people: ac + people['age'], people, 0)

print(f'average age: { add_age / len(people) }')
