'''
    → Dictionaries are structures that comprise a set of key and value pairs.
    → Are changeable

    → When to use?
        We must use dictionaries when there is a need to store data in an organized 
        way, since with the dictionary it is possible to map the value of an element 
        with a unique key.
'''

# declare
# name = { key: value }

students = {
    1: 'Raul',
    2: 'André',
    3: 'Santiago',
}

students = dict(
    key1='Raul',
    key2='André',
)

# get
students.get(1)

# update - use to update or concatenate dictionaries
students.update({
    4: 'Maria'
})

# del
del students[4]

# check exist key or value in dictionary
print(2 in students)                # keys
print(2 in students.keys())         # keys
print(2 in students.values())       # values

# iteration
for key, value in students.items():
    print(key, value)

# shallow copy
s = students.copy()

# deep copy
import copy

s = copy.deepcopy(s)

# casting
numbers = [
    [1, '1'],
    [2, '2'],
    [3, '3'],
    (4, '4'),
]

numbers = dict(numbers)

# pop - remove with key
numbers.pop(1)

# popitem - remove last item
numbers.popitem()