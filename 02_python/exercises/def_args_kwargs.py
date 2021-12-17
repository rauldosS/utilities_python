'''
1 - Create a function1 that receives a function2 as a parameter and returns the value 
of the function2 executed.
'''

def hello_world():
    return 'Hello world!'


def master(role):
    return function()


print(hello_world())

'''
2 - Create a function1 that receives a function2 as a parameter and returns the value 
of the function2 executed. Have function1 execute two functions that take a different 
number of arguments.
'''

def master(func, *args, **kwargs):
    return func(*args, **kwargs)

def hello(nome):
    return f'Oi {nome}'

def salutation(nome, salutation):
    return f'{salutation} {nome}'


exec = master(hello, 'Luiz')
exec2 = master(salutation, 'Luiz', salutation='Bom dia!')

print(exec)
print(exec2)