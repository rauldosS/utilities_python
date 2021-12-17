'''
    → Types of association:
        → Association - Use
        → Aggregation - Has
        → Membership - Owns
        
composition
'''

# Association
# One class is related to another but neither class depends on the other.

class Writer:
    def __init__(self, name):
        self.__name = name
        self.__tool = None

    @property
    def name(self):
        return self.__name

    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool):
        self.__tool = tool

class Pen:
    def __init__(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    def write(self):
        print('Pen is writing')

class TypeWriter:
    def write(self):
        print('Typewriter is writing')

# Aggregation
# A class uses another class as part of itself and this class needs the other class.

''' 💡 Example 
        → Cars and wheels
            → Are independent but the car needs the wheels to work properly
'''

# Shopping Cart can exist alone but not carry out options without products

class shoppingCart:
    def __init__(self):
        self.products = []

    def insertProcut(self, product):
        self.products.append(product)

    def get_products(self):
        for product in self.products:
            print(product.name, product.price)

    def sum_total(self):
        return sum([product.price for product in self.products])

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Composition
# A class will own objects of another class.

''' 💡 Example 
        → Customer registration
            → Are independent but the car needs the wheels to work properly
'''

class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.addresses = []

    def insertAddress(self, city, state):
        self.addresses.append(Address(city=city, state=state))

    def getAddresses(self):
        for address in self.addresses:
            print(address.city, address.state)

    def __del__(self):
        print(f'{ self.name} delete!')

class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):
        print(f'{ self.city } delete!')