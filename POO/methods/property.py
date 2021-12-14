'''
    → @property - Getters and Setters

    → getter
        → get value

    → setter
        → assign value
'''

# 💡 class Product
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percentage):
        self.price = self.price - (self.price * (percentage / 100))

    # Getter
    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('$', ''))

        self._price = value

    @name.setter
    def name(self, value):
        self._name = value

keyboard = Product('Keyboard', 50)
mouse = Product('Mouse', '$40')

print(f'{ keyboard.name }: { keyboard.price }')
print(f'{ mouse.name }: { mouse.price }')

mouse.discount(10)
print('After discount')
print(f'{ keyboard.name }: { keyboard.price }')
print(f'{ mouse.name }: { mouse.price }')

# 💡 
# 💡 
# 💡 
# 💡 