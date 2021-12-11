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

# 💡 
# 💡 
# 💡 
# 💡 
# 💡 
# 💡 