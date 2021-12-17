'''
    → Metaclass

    IN PYTHON EVERYTHING IS AN OBJECT: including classes

    Metaclass are the "classes" that create classes.

    type is a metaclass !!!???
'''

# Example

# Create a normal class that inherits from type
class Meta(type):
    # mcs           metaclass
    # name          Name
    # bases         Parent classes
    # namespace     All atributes and methods from class
    def __new__(mcs, name, bases, namespace):
        print('\nmcs:', mcs)
        print('name:', name)
        print('bases:', bases)
        print('namespace:', namespace)

        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        # Forces the creation of the class on all inheritances, similar to the abstract method
        if 'speak' not in namespace:
            print(f'\nNeed to create speak method in { namespace }')
        else:
            # Check if it is a method
            if not callable(namespace['speak']):
                print(f'\nSpeak must be a method on { name }')

        # Do not allow an attribute to be overwritten
        if 'attr_class' in namespace:
            del namespace['attr_class']

        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta):
    attr_class = 'Value A'

    def speak(self):
        self.b_speck()

class B(A):
    attr_class = 'Value B'

    def speak(self):
        self.b_speck()

a = A()
b = B()

print(b.attr_class)

# how to use type to create classes
# name=A, who inherits=(), attributes=namespace
A = type('A', (), { 'attr': 'Hello World!' })

a = A()

print(a.attr)
print(type(A))

# 
# 
# 
# 