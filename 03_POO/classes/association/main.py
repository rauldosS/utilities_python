from classes import Writer, Pen, TypeWriter, shoppingCart, Product, Client, Address

# Association
writer = Writer('Clarice Lispector')
pen = Pen('Bic')
type_writer = TypeWriter()

writer.tool = pen
writer.tool.write()

# Aggregation
cart = shoppingCart()

keyboard = Product('Keyboard', 50)
mouse = Product('Mouse', 40)
monitor = Product('Mouse', 200)

cart.insertProcut(keyboard)
cart.insertProcut(mouse)
cart.insertProcut(monitor)

print('Total: $', cart.sum_total())

# Composition
client1 = Client('Raul', 22)
client2 = Client('Maria', 32)

client2.insertAddress('Caçador', 'SC')

client1.insertAddress('Caçador', 'SC')
client1.insertAddress('Blumenau', 'SC')

print(client1.getAddresses())
print(client2.getAddresses())

del client1