'''
    → Dictionary Comprehension
'''

# declare
l1 = [
    ('key', 'value'),
    ('key2', 'value2'),
]

d1 = {x: y for x, y in l1}
d1 = {f'key_{ x }': x**2 for x in range(5)}