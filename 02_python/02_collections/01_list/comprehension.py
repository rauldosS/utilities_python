'''
    → List Comprehension
'''

# declare
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

example = [variable for variable in l1]

# multiplication
example = [v * 2 for v in l1]

# tuple
example = [(v, v2) for v in l1 for v2 in range(3)]

tuple1 = (
    ('key', 'value'),
    ('key2', 'value2'),
)

example = [(x, y) for x, y in tuple1]

# names
names = ['Raul', 'André', 'John', 'Lucas']
example = [name.replace('a', '@').upper for name in names]

# others examples
l1 = list(range(100))
example = [v for v in l1 if v % 2 == 0]
example = [v for v in l1 if v % 3 == 0 if v % 8 == 0]

example = [v if v % 2 == 0 else 'It is not' for v in l1]

# exercises
string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'

n = 10
lista = [string[i:i + n] for i in range(0, len(string), n)]

print(lista)
print('.'.join(lista))