'''
    → Combinations
    
    →  Order imports and repeats single values
'''

# import
from itertools import product

# declare
people = ['Raul', 'André', 'John', 'Lucas']

for group in product(people, repeat=2):
    print(group)