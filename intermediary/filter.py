import sys

sys.path.append('../data')

from data import products, people, numbers

# 💡 numbers greater than 5
new_numbers = filter(lambda x:x > 5, numbers)

print(list(new_numbers))
# 💡 Products with a price greater than 50
new_products = filter(lambda product: product['price'] > 50, products)

print(list(new_products))

# 💡 

# 💡 
# 💡 
# 💡 
# 💡 
