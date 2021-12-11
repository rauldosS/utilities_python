''' 💡 
1 - Create a function that displays a greeting with the greeting and name parameters.
'''

def salutation(name='Raul', message='Hello!'):
    return print(f'{ name }, { message }')

salutation()
salutation('Andre')
salutation(message='Tchau!')


''' 💡 
2 - Create a function that takes 3 numbers as parameters and displays the sum between them.
'''

def sum(n1, n2, n3):
    print(n1 + n2 + n3)


sum(2, 1, 3)
sum(1, 1, 1)
sum(2, 1, 1)

''' 💡 
3 - Create a function that receives 2 numbers. The first is a value
and the seconds a percentage (eg 10%). Return (return) the value of the first
number added by its percentage increase.
'''

def percentage_increase(valor, percentual):
    return valor + (valor * percentual / 100)

ap = percentage_increase(50, 10)
print(ap)
ap = percentage_increase(100, 10)
print(ap)
ap = percentage_increase(10, 10)
print(ap)
ap = percentage_increase(15, 100)
print(ap)


''' 💡 
4 - Fizz Buzz - If the function parameter is divisible by 3, return fizz, 
if the function parameter is divisible by 5, return buzz. If the function 
parameter is divisible by 5 and by 3, return FizzBuzz, otherwise, return 
the sent number.
'''


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} is divisible by 3 and 5'
    if n % 5 == 0:
        return f'buzz, {n} is divisible by 5'
    if n % 3 == 0:
        return f'fizz, {n} is divisible by 3'
    return n


from random import randint

for i in range(100):
    r = randint(0, 100)
    print(fb(r))
