'''
    → Zip and Zip_longest
    → Uniting iterables
'''

# zip - Joins to the shortest list
cities = ['Caçador', 'Videira', 'Joaçaba', 'São Paulo']
states = ['SC', 'MG', 'BA']

cities_states = zip(cities, states)

# zip_longest - Joins to the biggest list
from itertools import zip_longest

cities_states = zip_longest(
    states,
    cities,
    fillvalue='State'
)

# count & zip
from itertools import count
indexes = count()

cities_states = zip(
    indexes,
    states,
    cities
)

for index, state, city in cities_states:
    print(index, state, city)