numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]

# 💡 declare
def salutation(name='Raul', message='Hello!'):
    return print(f'{ name }, { message }')

def division(n1, n2):
    if n2 == 0:
        return print('Não é possível dividir por 0')
    return print(n1 / n2)

# 💡 call/execute

salutation()
salutation('Andre')
salutation(message='Tchau!')

division(10, 5)
division(10, 0)

# 💡 *args
def func(*args, **kwargs):
    print(args)
    print(kwargs.get('name'))
    # print(args[0])
    # print(args[-1])
    # print(len(args))

func(*numbers1, *numbers2, name='Raul')

# 💡 **kwargs


# 💡 
# 💡 
# 💡 
# 💡 