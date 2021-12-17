from data import products, people, numbers

# map - return iterator
new_numbers = map(lambda x: x * 2, numbers)

print(list(new_numbers))

# map with dictionary 

# get prices products
prices = map(lambda product: product['price'], products)

print(list(prices))

# update price products in 5%
def update_price(product):
    product['price'] = round(product['price'] * 1.05, 2)
    return product

new_procuts = map(update_price, products)

print(list(new_procuts))

# create list with map
names = map(lambda people: people['name'], people)

print(list(names))