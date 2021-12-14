'''
    → Decorators

    → A decorator in Python is an object that extends/modifies the functionality of a 
    function (or method) at runtime and is conceptually closer to Java annotation than 
    to the object-oriented decorator.

    → They are used extensively to extract common code that must be applied to various functions.
'''

# 💡 decorators
def master(function):
    def slave(*args, **kwargs):
        function()

    return slave

@master # This is a decorator
def hello():
    print('Hello World!')

hello()


# 💡 speed
from time import time
from time import sleep

def speed(function):
    def internal(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        
        elapsed_time = (end_time - start_time) * 1000

        print(f'The function { function.__name__ } took { elapsed_time }ms to run.')

        return result
    return internal

@speed
def delay():
    for i in range(1000):
        print(i, end='')
        # sleep(1)

delay()