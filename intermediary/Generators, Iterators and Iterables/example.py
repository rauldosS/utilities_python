'''
    → Generators, unlike lists, do not allocate all values in memory.
    → It will return the value only when requested.

    → Lists, tuples and str → Sequences → Iterables
        → FOR loop → next()

    → Generators → iter()
        → 
'''


numbers = list(range(10))

# 💡 Iterables
print(hasattr(numbers, '__iter__'))

# 💡 Iterators 
numbers = iter(numbers)
print(hasattr(numbers, '__next__'))

print(next(numbers)) # 0
print(next(numbers)) # 1
print(next(numbers)) # 2

# 💡 bytes consumed
import sys

numbers = list(range(1000000))

print(f'{ sys.getsizeof(numbers) } bytes')

# 💡 Generator range
def generate_range():
    for n in range(100):
        yield n

g = generate_range()

for v in g:
    print(v)

# 💡 Generator variable
def generate_variable():
    variable = 'value 1'
    yield variable

    variable = 'value 2'
    yield variable

    variable = 'value 3'
    yield variable

g = generate_variable()

print(next(g)) # value 1
print(next(g)) # value 2
print(next(g)) # value 3

# 💡 Compare
numbers_list = [x for x in range(1000)]
numbers_generator = (x for x in range(1000))

print(f'{ sys.getsizeof(numbers_list) } bytes ({ type(numbers_list) })')
print(f'{ sys.getsizeof(numbers_generator) } bytes ({ type(numbers_generator) })')

##############################
# 💡 Behavior Iterator and generator
name = 'Raul dos Santos Moraes'
iterator = iter(name)
generator = (letter for letter in name)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# FOR LOOP will display the rest of the iterations
print('Other itens')
for letter in generator:
    print(letter)

# 💡 Behavior Iterable
'''
    'When using them as iterators they will be converted to runtime and consumed.
'''