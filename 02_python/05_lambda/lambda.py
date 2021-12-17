''' 💡 When to use?
        → Passing a function as a parameter to another function
        → Order
'''

# declare def
def multiplication(num1, num2):
    return num1 + num2

# declare
multiplication_lambda = lambda x, y: x * y

print(multiplication_lambda(2, 2))

# order sort()
products = [
    ['P1', 13],
    ['P2', 3],
    ['P3', 42],
    ['P4', 31],
    ['P5', 3],
]

def key(item):
    return item[1]

products.sort(key=key, reverse=True)

# order lambda
products.sort(key=lambda item: item[1], reverse=False)

# sorted
sorted(products, key=lambda item: item[1], reverse=True)