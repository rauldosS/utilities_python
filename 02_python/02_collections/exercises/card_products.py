'''
    → Add total value of products with understanding of lists
'''
cart = []

cart.append(('Produto 1', 30))
cart.append(('Produto 2', 50))
cart.append(('Produto 3', 30))

total = sum([value for product, value in cart])

print(total)

# Valor base no produto
# Valor pode ser alterado na derivação