'''
    → It is a structure of indexed data stored in sequence, where each element has a 
    position that is identified by an index.

    → lists are changeable
    → Are accessible through the index

    → When to use?
        It is recommended to use lists when working with homogeneous structures, that is, 
        when all elements are of the same type (strings, int, float, etc.), and/or when 
        there is a need to change the items in the collection.
'''

# declare
# index       0    1    2    3    4
letters =   ['A', 'B', 'C', 'D', 'E']
l1 =        [1,    2,   3]
l2 =        [4,    5,   6]
# index      5     4    3    2    1

l3 = list(range(100)) # list with 100 values

# slicing
print('Index 1:', letters[1])
print('Index 2 to 4: ', letters[2:4])

# append
letters.append('F')

# +
l3 = l1 + l2

# del
del(letters[1])

# insert(index, value)
letters.insert(1, 'B')

# extend
l1.extend(l2)

# pop() - remove last index
letters.pop()

# min(list), max(list), sum(list)
print( max(letters) )
print( min(letters) )
print( sum(letters) )

# range
l2 = list(range(1, 100, 8))
print(l2)

for value in l2:
    print(value)

# clear
letters.clear()

# enumerate(list, first_index) - unpacking a simple list
for index, value in enumerate(letters):
    print(index, value)

people = [
    [0, 'Raul'],
    [1, 'Maria'],
    [2, 'André'],
]

for index, value in people:
    print(index, value)

# unpacking lists
people = ['Raul', 'Maria', 'André', 'Mauro', 'Adriano']

n1, n2, *other_people, last_people = people

print(n1, n2, other_people, last_people)