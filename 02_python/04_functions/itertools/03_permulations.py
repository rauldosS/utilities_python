'''
    → Combinations
    → Order matters
    → Does not repeat single values
'''

# import
from itertools import permutations

# declare
people = ['Raul', 'André', 'John', 'Lucas']

for group in permutations(people, 2):
    print(group)