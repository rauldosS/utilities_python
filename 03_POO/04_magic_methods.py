'''
    → A Guide to Python's Magic Methods
        → https://rszalski.github.io/magicmethods/
'''

# import
class A:
    def __new__(cls, *args, **kwargs):
        '''
            → All classes derive from object

            → it is the same as
                return object().__new__(cls)
        '''
        # design pattern singleton (uniqui instance)
        if not hasattr(cls, '_exists'):
            cls._exists = object.__new__(cls)

        return cls._exists

        # Example of random possibilities
        def hello(*args, **kwargs):
            print('Hello World!')
        
        cls.hello = hello

        # return new instance
        return super().__new__(cls)

    # make class behave like function
    def __call__(self, *args, **kwargs):
        print('args:', args)
        print('kwargs:', kwargs)

        result = 1

        for i in args:
            result *= i

        print('result:', result)

    # called after __new__
    def __init__(self):
        print('INIT')

    def __setattr__(self, key, value):
        if key == 'any':
            self.__dict__[key] = 'You can not do that'
        else:
            self.__dict__[key] = value

    def __len__(self):
        return 55

    def __del__(self):
        print('Collected object')

# __init__ and __new__
'''
    a = A()
    b = A()
    c = A()

    # a.hello()

    print(a == b == c)
    print(id(a), id(b), id(c))
'''

# __call__
a = A()

a(1, 2, 3, 4, 5, 6, 7, 8, 9, name='Raul', surname='Moraes')
    # args: (1, 2, 3, 4, 5, 6, 7, 8, 9)
    # kwargs: {'name': 'Raul'}

# __setattr__
a.name = 'Raul'
a.any = 'Moraes'

print('any:', a.any)
print('name:', a.name)

# __len__
print(len(a))