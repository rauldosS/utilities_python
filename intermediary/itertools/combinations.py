'''
    → Combinations
    → Order does not matter
    → Does not repeat single values
'''

# 💡 import
from itertools import combinations

# 💡 declare
people = ['Raul', 'André', 'John', 'Lucas']

for group in combinations(people, 2):
    print(group)