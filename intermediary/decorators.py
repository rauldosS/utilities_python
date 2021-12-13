'''
    → 
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